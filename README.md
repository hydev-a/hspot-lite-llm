
### **README.md**

# 🕵️ Hallucination Spotter

A lightweight Python library for detecting hallucinations in LLM outputs without API calls.

## 🔍 Features
- **Contradiction Detection**: Identifies conflicting numerical claims  
- **Vague Language Flagging**: Catches unsourced assertions  
- **Temporal Validation**: Detects impossible dates  
- **Risk Scoring**: 0-1 scale with configurable thresholds  

## 🚀 Quickstart
```bash
pip install hallucination-spotter
python -m spacy download en_core_web_sm
```

```python
from hallucinator import HallucinationDetector

detector = HallucinationDetector()
results = detector.analyze("The budget was $5M in 2022 and $5M in 2023")
print(f"Risk: {results['risk_score']:.2f}")
```

## 📋 CLI Usage
```bash
hspot "Some experts claim the event happened on February 30th" --threshold 0.7
```

## 📚 Documentation
- [Detection Rules](hallucination-spotter/docs/detection_rules.md)  
- [Advanced Configuration](hallucination-spotter/docs/quickstart.md)  

<sub>⚡ No API costs • 100% local execution • MIT Licensed</sub>

**Examples**:  
- `"Some studies suggest..."` → **Flagged**  
- `"NASA confirmed..."` → **Ignored**  

