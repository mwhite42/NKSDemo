from aiohttp import web


async def handle(request):
    return web.json_response({"reflection": str(request.rel_url.query)})


app = web.Application()
app.router.add_get('minimum/v1/', handle)

web.run_app(app)
