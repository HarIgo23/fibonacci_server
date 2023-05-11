from typing import Any

from aioredis import Redis


CLIENTS: dict[str, Any] = {}


def get_redis() -> Redis:
    """Returns Redis client."""
    return CLIENTS["redis"]
