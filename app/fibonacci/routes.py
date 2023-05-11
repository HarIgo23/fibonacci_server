from fibonacci.views import index, fibonacci


def init_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/fibonacci', fibonacci)
