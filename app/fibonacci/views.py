from aiohttp import web

from fibonacci.exceptions import IncorrectFibonacciParams
from fibonacci.fibonacci import cached_fibonacci_sequence


async def index(request: web.Request) -> web.Response:
    """Return description of site."""
    return web.Response(
        text="""
        Endpoints:                                                                              \n
        - /fibonacci endpoint returns sequence of fibonacci from `from` to `to`                 \n
        - - params:                                                                             \n
        - - - `from`'element of sequence                                                        \n
        - - - `to`'element of sequence                                                          \n
        - - example:                                                                            \n
        - - - fibonacci?from=3&to=6 return [2, 3, 5]                                            \n
        - - explain:                                                                            \n
        - - - In mathematics, the Fibonacci sequence is a sequence in which each number         \n
        - - - is the sum of the two preceding ones. The sequence commonly starts from 0 and 1.  \n
        - - - So, Usually 0 is F_0 and 1 is F_1.                                                \n
        """
    )


async def fibonacci(request: web.Request) -> web.Response:
    """Return fibonacci sequence."""
    data = {}
    try:
        from_param, to_param = _get_fibonacci_params(request)
    except IncorrectFibonacciParams as e:
        data["error"] = str(e)
        return web.json_response(data)

    data["data"] = await cached_fibonacci_sequence(from_param, to_param)
    return web.json_response(data)


def _get_fibonacci_params(request: web.Request) -> tuple[int, int]:
    """Trying to get params for fibonacci."""
    from_param = request.rel_url.query.get('from', None)
    to_param = request.rel_url.query.get('to', None)

    if from_param is None or to_param is None:
        raise IncorrectFibonacciParams("from and to params are required")

    try:
        from_param = int(from_param)
        to_param = int(to_param)
    except ValueError:
        raise IncorrectFibonacciParams("from and to params must be integer numbers")

    return from_param, to_param
