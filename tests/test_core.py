import pytest
from hallucinator.core import HallucinationDetector

TEST_CASES = [
    (
        "The project started in 2022 and ended in 2022.", 
        {
            'contradictions': [],
            'vague_phrases': [],
            'unverifiable_claims': ['2022', '2022'],
            'invalid_dates': []
        }
    ),
    (
        "Some experts believe the temperature reached 500°C on February 30th.",
        {
            'contradictions': [],
            'vague_phrases': ['Some experts'],
            'unverifiable_claims': ['February 30th'],
            'invalid_dates': ['February 30th']
        }
    )
]

@pytest.fixture
def detector():
    return HallucinationDetector()

@pytest.mark.parametrize("text,expected", TEST_CASES)
def test_detection_logic(text, expected, detector):
    results = detector.analyze(text)
    
    assert results['contradictions'] == expected['contradictions']
    assert results['vague_phrases'] == expected['vague_phrases']
    assert set(results['unverifiable_claims']) == set(expected['unverifiable_claims'])
    assert results['invalid_dates'] == expected['invalid_dates']

def test_risk_score_calculation(detector):
    text = "Multiple reports state 10 people attended. Other sources say 10 participants."
    results = detector.analyze(text)
    assert 0.4 <= results['risk_score'] <= 0.6