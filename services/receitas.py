from models.models import Receitas

def create_recipe(payload: dict) -> None:
    recipe = Receitas(
        titulo = payload["titulo"],
        ingredientes = payload["ingredientes"],
        preparo = payload["preparo"],
        img = payload["img"]
    )
    recipe.save()


def find_recipe_by_id(id: int) -> dict:
    recipe = Receitas.query.filter_by(id=id).first()
    return { 
        "titulo": recipe.titulo,
        "ingredientes": recipe.ingredientes,
        "preparo": recipe.preparo,
        "img": recipe.img
    }


def find_recipe_by_name(name: str) -> dict:
    recipe = Receitas.query.filter_by(titulo=name).first()
    return { 
        "titulo": recipe.titulo,
        "ingredientes": recipe.ingredientes,
        "preparo": recipe.preparo,
        "img": recipe.img
    }


def get_recipe_db(id: int) -> Receitas:
    return Receitas.query.filter_by(id=id).first()


def find_all_recipes() -> list:
    list_recipes = []
    recipes = Receitas.query.all()
    for recipe in recipes:
        list_recipes.append(
            {
                "titulo": recipe.titulo,
                "ingredientes": recipe.ingredientes,
                "preparo": recipe.preparo,
                "img": recipe.img 
            }
        )
    return list_recipes
    

def update_recipe(id, payload: dict) -> None:
    recipe = get_recipe_db(id)
    recipe.titulo = payload["titulo"]
    recipe.ingredientes = payload["ingredientes"]
    recipe.preparo = payload["preparo"]
    recipe.img = payload["img"]
    recipe.update()


def delete_recipe(id: int) -> None:
    recipe = get_recipe_db(id)
    recipe.delete()