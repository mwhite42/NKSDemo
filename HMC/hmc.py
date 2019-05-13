from aiohttp import web  # Use the AIO Http Lib

import os
import aiohttp_jinja2
import jinja2
import datetime

PRESENTER = os.environ.get('PRESENTER', "Unknown")
ENV = os.environ.get('ENVIRONMENT', "unknown")


# Handle a request mapped from the URL below and process it through the template
@aiohttp_jinja2.template('./templates/index.jinja2')
async def handle(request):
    now = datetime.datetime.now()
    return {"presenter": PRESENTER, "date": now.strftime("%Y%m%d%H%M%S"), "env": ENV}


async def mp4(request):
    return web.FileResponse('/static/hmc.mp4')


app = web.Application()  # Initialize the base web application
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(''))  # tell the template system where to look for templates

app.router.add_get('/', handle)  # Configure a URL
app.router.add_static("/css/", path="./css/")
app.router.add_get("/hmc.mp4", mp4)

web.run_app(app)  # Loop and listen for connections
