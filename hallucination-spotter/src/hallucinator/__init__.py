"""
Hallucination detection for LLM outputs
"""

__version__ = "0.1.0"

from .core import HallucinationDetector
from .cli import main

__all__ = ["HallucinationDetector", "main"]