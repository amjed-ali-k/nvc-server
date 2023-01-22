from fastapi import Body, APIRouter

from app.model import RecipeSchema, UpdateRecipeSchema
from app.database.recipies import (
    save_recipe,
    get_all_recipes,
    get_single_recipe,
    update_recipe_data,
    remove_recipe,
)

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("/recipe")
def get_recipes() -> dict:
    recipes = get_all_recipes()
    return {"data": recipes}


@router.get("/recipe/{id}")
def get_recipe(id: str) -> dict:
    recipe = get_single_recipe(id)
    if recipe:
        return {"data": recipe}
    return {"error": "No such recipe with ID {} exist".format(id)}


@router.post("/recipe")
def add_recipe(recipe: RecipeSchema = Body(...)) -> dict:
    new_recipe = save_recipe(recipe.dict())
    return new_recipe


@router.put("/recipe")
def update_recipe(id: str, recipe_data: UpdateRecipeSchema) -> dict:
    if not get_single_recipe(id):
        return {"error": "No such recipe exist"}

    update_recipe_data(id, recipe_data.dict())

    return {"message": "Recipe updated successfully."}


@router.delete("/recipe/{id}")
def delete_recipe(id: str) -> dict:
    if not get_single_recipe(id):
        return {"error": "Invalid ID passed"}

    remove_recipe(id)
    return {"message": "Recipe deleted successfully."}
