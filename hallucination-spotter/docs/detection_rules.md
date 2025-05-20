### **docs/detection_rules.md**

# 🔬 Detection Rules

## 1. Contradictions
**Trigger**: Same number in conflicting contexts  
**Example**:  
`"The budget was $5M in 2022 and $5M in 2023"`  
→ Flags `('5', 2)`  

**Technical**:  
- Regex: `\b\d+\b`  
- Minimum repeats: 2 (configurable)  

## 2. Vague Language
**Patterns**:  
```python
r"\b(some\s+experts|studies\s+show|anonymous\s+sources|it\s+is\s+believed)\b"
```
