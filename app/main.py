from aiohttp import web

from aioredis import Redis, from_url

from config import ENABLE_WARMUP, FIBONACCI_LIST_NAME, WARMUP_CACHE_LEN
from dependencies import CLIENTS, get_redis
from fibonacci.routes import init_routes
from fibonacci.fibonacci import fibonacci_sequence


async def init_redis(app: web.Application) -> None:
    """Initialise redis connection."""
    redis: Redis = from_url("redis://redis")

    await redis.ping()

    CLIENTS["redis"] = redis


async def warmup_redis(app: web.Application) -> None:
    """Generate and add first WARMUP_CACHE_LEN elements to cache."""
    redis = get_redis()

    seq_len = await redis.llen(FIBONACCI_LIST_NAME)
    if seq_len != 0:
        return

    sequence = fibonacci_sequence(WARMUP_CACHE_LEN)
    await redis.rpush(FIBONACCI_LIST_NAME, *sequence)


async def close_redis(app: web.Application) -> None:
    """Clean up redis connection."""
    redis: Redis = get_redis()
    await redis.close()


def init_app(argv=None) -> web.Application:
    """Initialize application."""
    app = web.Application()
    init_routes(app)

    startup_tasks = [init_redis]
    if ENABLE_WARMUP:
        startup_tasks.append(warmup_redis)
    app.on_startup.extend(startup_tasks)
    app.on_cleanup.extend([close_redis])

    return app


app = init_app()
