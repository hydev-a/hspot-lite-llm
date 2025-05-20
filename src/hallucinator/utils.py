from typing import Union
from pathlib import Path

def validate_input(input: Union[str, Path]) -> str:
    """Validate and normalize input text"""
    if isinstance(input, Path) or Path(input).exists():
        with open(input, "r", encoding="utf-8") as f:
            return f.read()
    return str(input)

def format_results(results: dict) -> str:
    """Format analysis results for display"""
    return "\n".join(
        f"{k.replace('_', ' ').title()}: {v}"
        for k, v in results.items()
    )