from aiohttp import web

operations = ["Combine flour, baking soda, and salt in small bowl. ",
              "Beat butter, granulated sugar, brown sugar, and vanilla extract in large mixer bowl until creamy. ",
              "Add eggs, one at a time, beating well after each addition. ",
              "Gradually beat in flour mixture. Stir in morsels and nuts. ",
              "Drop by rounded tablespoon onto ungreased baking sheets."]


async def steps(request):
    print("Steps")
    return web.json_response(operations)


async def stepcount(request):
    print("Step Count")
    return web.json_response({"step count": operations.count()})


async def stepone(request):
    print("Step One")
    return web.json_response({"Step 1", operations[0]})


async def steptwo(request):
    print("Step Two")
    return web.json_response({"Step 2", operations[1]})


async def stepthree(request):
    print("Step Three")
    return web.json_response({"Step 3", operations[2]})


async def stepfour(request):
    print("Step Four")
    return web.json_response({"Step 4", operations[3]})


async def stepfive(request):
    print("Step Five")
    return web.json_response({"Step 5", operations[4]})

print("Starting Up /preparation/v1")
app = web.Application()
app.router.add_get('/preparation/v1/', steps)
app.router.add_get('/preparation/v1/steps', steps)
app.router.add_get('/preparation/v1/stepcount', stepcount)
app.router.add_get('/preparation/v1/stepone', stepone)
app.router.add_get('/preparation/v1/steptwo', steptwo)
app.router.add_get('/preparation/v1/stepthree', stepthree)
app.router.add_get('/preparation/v1/stepfour', stepfour)
app.router.add_get('/preparation/v1/stepfive', stepfive)

web.run_app(app)
