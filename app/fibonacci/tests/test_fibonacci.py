import pytest

from fibonacci.fibonacci import fibonacci_sequence
from fibonacci.exceptions import IncorrectFibonacciSequence


def test_first_five():
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]


def test_custom_range():
    assert fibonacci_sequence(5, 377, 610) == [377, 610, 987, 1597, 2584]


def test_incorrect_sequence():
    with pytest.raises(IncorrectFibonacciSequence):
        fibonacci_sequence(1)
