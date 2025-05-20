import subprocess
import pytest
import tempfile
from pathlib import Path

def test_cli_with_text_input():
    result = subprocess.run(
        ["hspot", "The event occurred on 2023-02-30"],
        capture_output=True,
        text=True
    )
    assert "invalid date" in result.stdout.lower()
    assert result.returncode == 1

def test_cli_with_file_input():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Some studies show temperatures reached 500°C")
    
    result = subprocess.run(
        ["hspot", f.name],
        capture_output=True,
        text=True
    )
    Path(f.name).unlink()
    
    assert "vague phrases: ['Some studies']" in result.stdout
    assert result.returncode == 1

def test_threshold_handling():
    result = subprocess.run(
        ["hspot", "Normal text without issues", "--threshold=0.5"],
        capture_output=True,
        text=True
    )
    assert "no significant issues" in result.stdout
    assert result.returncode == 0