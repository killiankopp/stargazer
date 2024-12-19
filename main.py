from fastapi import FastAPI
from starlette import status

from src.starneighbours import get_starneighbours

app = FastAPI()


@app.get("/repos/{user}/{repo}/starneighbours", status_code = status.HTTP_200_OK)
async def starneighbours(user: str, repo: str):
    return get_starneighbours(user, repo)
