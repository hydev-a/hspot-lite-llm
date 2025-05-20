import argparse
import sys
from pathlib import Path
from hallucinator.core import HallucinationDetector

def main():
    """Command-line interface entry point"""
    parser = argparse.ArgumentParser(
        description="Detect potential hallucinations in text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "input",
        help="Input text or path to .txt file",
        type=str
    )
    parser.add_argument(
        "--threshold", 
        help="Risk score threshold for warning",
        type=float,
        default=0.5
    )
    
    args = parser.parse_args()
    detector = HallucinationDetector()
    
    # Handle file input
    if Path(args.input).exists():
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError:
            print(f"Error: Could not read {args.input} as UTF-8 text")
            sys.exit(1)
    else:
        text = args.input
    
    results = detector.analyze(text)
    
    print("\nHallucination Analysis Report")
    print("=" * 30)
    print(f"Contradictions: {results['contradictions']}")
    print(f"Vague Phrases: {results['vague_phrases']}")
    print(f"Unverifiable Claims: {results['unverifiable_claims']}")
    print(f"Invalid Dates: {results['invalid_dates']}")
    print(f"\nOverall Risk Score: {results['risk_score']:.2f}")
    
    if results['risk_score'] >= args.threshold:
        print("\n⚠️  Warning: High hallucination risk detected!")
        sys.exit(1)
    else:
        print("\n✅ No significant issues detected")
        sys.exit(0)