from fibonacci.exceptions import IncorrectFibonacciSequence


def fibonacci_sequence(n: int, first: int = 0, second: int = 1) -> list[int]:
    """Returns n elements from Fibonacci sequence.

    :param n(int) length of sequence, strictly more than 2
    :param first(int) first element of sequence
    :param second(int) second element of sequence

    :exception IncorrectFibonacciSequence if n < 2
    """
    if n < 2:
        raise IncorrectFibonacciSequence

    res = [first, second]

    for i in range(2, n):
        res.append(res[i - 2] + res[i - 1])

    return res

