from blacksheep import get


@get("/")
async def index():
    return "Home"
