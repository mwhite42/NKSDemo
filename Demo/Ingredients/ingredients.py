from aiohttp import web


async def handle(request):
    return web.json_response({"reflection": str(request.rel_url.query)})


async def itemlist(request):
    items = {"ingredients": ["2 1/4 cups all-purpose flour",
                             "1 teaspoon baking soda",
                             "1 teaspoon salt",
                             "1 cup (2 sticks) butter, softened",
                             "3/4 cup granulated sugar",
                             "3/4 cup packed brown sugar",
                             "1 teaspoon vanilla extract",
                             "2 large eggs",
                             "2 cups Nestlé Toll House Semi-Sweet Chocolate Morsels",
                             "1 cup chopped nuts"]
             }
    return web.json_response(items)


async def flour(request):
    return web.json_response(["flour", "all-porpose", "2.24 cups"])


async def sugar(request):
    return web.json_response(["sugar", "white", "granulated", ".75 cups", "sugar", "brown", "packed", ".75 cups"])


async def soda(request):
    return web.json_response(["baking", "soda", "1 teaspoon"])


async def salt(request):
    return web.json_response(["salt", "1 teaspoon"])


async def eggs(request):
    return web.json_response(["eggs", "large", 2])


async def nuts(request):
    return web.json_response(["nuts", "chopped", "1 cup"])


async def chips(request):
    return web.json_response(["chips", "Semi-Sweet", "chocolate", "2 cups"])


async def vanilla(request):
    return web.json_response(["vanilla", "extract", "1 teaspoon"])


app = web.Application()
app.router.add_get('/ingredients/v1/', itemlist)
app.router.add_get('/ingredients/v1/list', itemlist)
app.router.add_get('/ingredients/v1/flour', flour)
app.router.add_get('/ingredients/v1/sugar', sugar)
app.router.add_get('/ingredients/v1/soda', soda)
app.router.add_get('/ingredients/v1/eggs', eggs)
app.router.add_get('/ingredients/v1/nuts', nuts)
app.router.add_get('/ingredients/v1/chips', chips)
app.router.add_get('/ingredients/v1/salt', salt)
app.router.add_get('/ingredients/v1/vanilla', vanilla)

web.run_app(app)
