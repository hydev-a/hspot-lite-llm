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

## 3. Unverifiable Claims
**Conditions**:  
✅ Named entities (PERSON/ORG/DATE)  
❌ Missing attribution verbs  

**Example**:  
`"Dr. Smith claimed the temperature reached 500°C"` → **Verifiable**  
`"Dr. Smith observed 500°C"` → **Unverifiable**  

## 4. Date Validation
**Invalid Patterns**:  
- February 30th  
- April 31st  
- 2023-02-29  

**Detection**: Hybrid of:  
1. `datefinder` library  
2. Custom day-month validation  
