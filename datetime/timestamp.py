from aiohttp import web
import datetime


async def handle(request):
    now = datetime.datetime.now()
    return web.json_response({"now timestamp": now.strftime("%Y%m%d%H%M%S")})


app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
