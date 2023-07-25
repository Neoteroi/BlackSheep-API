from typing import List

from blacksheep import get, post


@get("/api/examples")
async def get_examples() -> List[str]:
    return list(f"example {i}" for i in range(3))


@post("/api/examples")
async def add_example(self, example: str):
    """
    Adds an example.
    """
