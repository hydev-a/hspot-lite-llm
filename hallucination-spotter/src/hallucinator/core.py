import re
import datefinder
from typing import Dict, List, Tuple
import spacy
from spacy.tokens import Doc
from typing import Dict, List, Tuple

class HallucinationDetector:
    
    
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.vague_patterns = re.compile(
            r"\b(some\s+experts|many\s+reports|studies\s+show|"
            r"it\s+is\s+(?:believed|thought)|research\s+indicates)\b",
            re.IGNORECASE
        )
        self.contradiction_threshold = 2  # Minimum identical numbers to flag
        self.date_pattern = re.compile(
        r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(of\s+)?(january|february|...)\s+(\d{4})?\b",
        re.IGNORECASE
        )

    def analyze(self, text: str) -> Dict:
        doc = self.nlp(text)
        
        contradictions = self._find_contradictions(text)
        vague = self._find_vague_phrases(text)
        unverifiable = self._find_unverifiable_claims(doc)
        invalid_dates = self._validate_dates(text)
        
        # Enhanced date validation
        if not invalid_dates:
            invalid_dates = self._find_impossible_dates(text)
        
        return {
            "contradictions": contradictions,
            "vague_phrases": vague,
            "unverifiable_claims": unverifiable,
            "invalid_dates": invalid_dates,
            "risk_score": self.calculate_risk_score(
                contradictions, vague, unverifiable, invalid_dates
            )
        }

    def _find_contradictions(self, text: str) -> List[Tuple[str, int]]:
        numbers = re.findall(r"\b\d+\b", text)
        return [(n, count) for n, count in 
                ((n, numbers.count(n)) for n in set(numbers))
                if count >= self.contradiction_threshold]
    
    def _find_vague_phrases(self, text: str) -> List[str]:

        return self.vague_patterns.findall(text)
    
    def _find_unverifiable_claims(self, doc: Doc) -> List[str]:

        claims = []
        for ent in doc.ents:
            if ent.label_ in ["DATE", "PERSON", "ORG", "GPE"]:
                if not self._has_supporting_context(ent):
                    claims.append(ent.text)
        return claims
    
    def _has_supporting_context(self, entity) -> bool:

        return any(token.text.lower() in {"according", "stated", "reported"}
                   for token in entity.sent)
    
    def _validate_dates(self, text: str) -> List[str]:

        invalid = []
        for match in datefinder.find_dates(text, strict=True):
            try:
                match.strftime("%Y-%m-%d")
            except ValueError:
                invalid.append(str(match))
        return invalid
    
    def calculate_risk_score(self, contradictions, vague, unverifiable, invalid_dates) -> float:

        weights = {
            "contradictions": 0.35,  
            "vague_phrases": 0.25,
            "unverifiable_claims": 0.25,
            "invalid_dates": 0.15
        }
        
        # Raw score calculation
        raw_score = (
            len(contradictions) * weights["contradictions"] +
            len(vague) * weights["vague_phrases"] +
            len(unverifiable) * weights["unverifiable_claims"] +
            len(invalid_dates) * weights["invalid_dates"]
        )
        
        # Sigmoid scaling for better distribution
        return 1 / (1 + 2.718 ** (-3 * (raw_score - 1.0)))  # Steeper curve

    def _find_impossible_dates(self, text: str) -> List[str]:
        impossible = []
        for match in self.date_pattern.finditer(text.lower()):
            day = int(match.group(1))
            month = match.group(3)
            
            if (month == "february" and day > 29) or \
            (month in ["april", "june", "september", "november"] and day > 30) or \
            (day > 31):
                impossible.append(f"{day} {month}")
        
        return impossible