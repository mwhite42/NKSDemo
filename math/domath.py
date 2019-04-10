from aiohttp import web


async def add(request):
    answer = int(request.rel_url.query['first']) + int(request.rel_url.query['second'])
    return web.json_response({"answer": answer})


async def subtract(request):
    answer = int(request.rel_url.query['first']) - int(request.rel_url.query['second'])
    return web.json_response({"answer": answer})


async def multiply(request):
    answer = int(request.rel_url.query['first']) * int(request.rel_url.query['second'])
    return web.json_response({"answer": answer})


async def divide(request):
    answer = int(request.rel_url.query['first']) / int(request.rel_url.query['second'])
    return web.json_response({"answer": answer})


app = web.Application()
app.router.add_get('/add', add)
app.router.add_get('/subtract', subtract)
app.router.add_get('/multiply', multiply)
app.router.add_get('/divide', divide)

web.run_app(app)
