import pytest

from fibonacci.fibonacci import fibonacci_sequence
from fibonacci.exceptions import IncorrectFibonacciSequence


def test_first_five() -> None:
    """Test that first five elements generated correctly."""
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]


def test_custom_range() -> None:
    """Test elements that generates not from start."""
    assert fibonacci_sequence(5, 377, 610) == [377, 610, 987, 1597, 2584]


def test_incorrect_sequence() -> None:
    """Check that incorrect number will be handled."""
    with pytest.raises(IncorrectFibonacciSequence):
        fibonacci_sequence(1)
