import sys
import os
# Ensure parent directory is in sys.path so logic_utils can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from logic_utils import check_guess

# Test that check_guess returns the correct hint for high/low guesses
@pytest.mark.parametrize("guess,secret,expected_outcome,expected_hint", [
    (15, 10, "Too High", "Go LOWER!"),   # Guess is higher than secret
    (5, 10, "Too Low", "Go HIGHER!"),    # Guess is lower than secret
])
def test_check_guess_high_low_hints(guess, secret, expected_outcome, expected_hint):
    outcome, message = check_guess(guess, secret)
    assert outcome == expected_outcome
    assert expected_hint in message

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
