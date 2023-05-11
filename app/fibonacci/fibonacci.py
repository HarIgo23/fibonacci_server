from fibonacci.exceptions import IncorrectFibonacciSequence

from redis.asyncio import Redis

from config import FIBONACCI_LIST_NAME
from dependencies import get_redis


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


async def cached_fibonacci_sequence(from_element: int, to_element: int) -> list[int]:
    """Return slice from `from` to `to` of sequence."""
    redis: Redis = get_redis()
    seq_len = await redis.llen(FIBONACCI_LIST_NAME)

    if from_element > seq_len or from_element < seq_len <= to_element:
        print("fr_elem > seq_len")
        lasts_two = await redis.lrange(FIBONACCI_LIST_NAME, -2, -1)
        if len(lasts_two) == 2:
            print(lasts_two)
            sequence = fibonacci_sequence(
                to_element - seq_len + len(lasts_two) + 1,
                int(lasts_two[0]),
                int(lasts_two[1])
            )
            print(sequence)
            await redis.rpush(FIBONACCI_LIST_NAME, *sequence[2:])
        else:
            sequence = fibonacci_sequence(to_element)
            await redis.rpush(FIBONACCI_LIST_NAME, *sequence)

    sequence = await redis.lrange(FIBONACCI_LIST_NAME, from_element, to_element + 1)
    sequence = [int(el) for el in sequence]

    return sequence
