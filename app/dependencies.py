from aioredis import Redis

CLIENTS: dict = {}


def get_redis() -> Redis:
    """Returns Redis client."""
    return CLIENTS["redis"]
