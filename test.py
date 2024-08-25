import pytest

# Sample function to simulate digital input (e.g., HIGH or LOW)
def read_digital_signal():
    return 1  # Simulate HIGH

# Pytest case to ensure the digital signal is either HIGH or LOW
def test_digital_signal_correct():
    signal = read_digital_signal()
    assert signal in [0, 1], "Digital signal is neither HIGH nor LOW!"
