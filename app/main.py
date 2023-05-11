from aiohttp import web

from aioredis import Redis, from_url


async def index(request):
    return web.Response(text="Hello, world")


def init_routes(app):
    app.router.add_get('/', index)


async def init_redis(app: web.Application) -> None:
    """
    Initialise redis connection
    """
    redis: Redis = from_url("redis://redis")

    await redis.ping()

    app['redis'] = redis


async def close_redis(app: web.Application) -> None:
    """
    Clean up redis connection
    """
    redis: Redis = app['redis']
    await redis.close()


def init_app(argv=None) -> web.Application:
    app = web.Application()
    init_routes(app)
    app.on_startup.extend([init_redis])
    app.on_cleanup.extend([close_redis])
    return app


app = init_app()
