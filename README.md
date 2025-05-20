
### **README.md**

#### ⚠️ Important note: This is a tiny project that was developed for learning and skill refining purposes, expect bugs and issues. I will work on refining and releasing it as a full python package when I have the time.

# 🕵️ Hallucination Spotter

A lightweight Python library for detecting hallucinations in LLM outputs without API calls.

## 🔍 Features
- **Contradiction Detection**: Identifies conflicting numerical claims  
- **Vague Language Flagging**: Catches unsourced assertions  
- **Temporal Validation**: Detects impossible dates  
- **Risk Scoring**: 0-1 scale with configurable thresholds  

## 🚀 Quickstart
```bash
git clone https://github.com/your-username/hallucination-spotter.git
cd hallucination-spotter
pip install -e .
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
- [Detection Rules](docs/detection_rules.md)  
- [Advanced Configuration](docs/quickstart.md)  

<sub>⚡ No API costs • 100% local execution • MIT Licensed</sub>

**Examples**:  
- `"Some studies suggest..."` → **Flagged**  
- `"NASA confirmed..."` → **Ignored**  

