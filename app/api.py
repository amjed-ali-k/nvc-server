from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from app.routes.recipies import router as RecipeRouter

app = FastAPI()
app.include_router(RecipeRouter)


@app.get("/", tags=["Root"])
def get_root() -> dict:
    return {"message": "Welcome to Napkin Vending Machine Server V2."}
