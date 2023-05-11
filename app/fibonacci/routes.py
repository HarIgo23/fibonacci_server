from aiohttp import web

from fibonacci.views import index, fibonacci


def init_routes(app: web.Application) -> None:
    """Initialize router."""
    app.router.add_get('/', index)
    app.router.add_get('/fibonacci', fibonacci)
