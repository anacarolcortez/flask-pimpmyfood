from models import Receitas

def create_recipe(payload: dict) -> None:
    recipe = Receitas(
        titulo = payload["titulo"],
        ingredientes = payload["ingredientes"],
        preparo = payload["preparo"]
    )
    recipe.save()


def find_recipe(id: int) -> Receitas:
    return Receitas.query.filter_by(id=id).first()
    

def find_all_recipes() -> [Receitas]:
    return Receitas.query.all()


def update_recipe(id: int, payload: dict) -> None:
    recipe = find_recipe(id)
    recipe.titulo = payload["titulo"]
    recipe.ingredientes = payload["ingredientes"]
    recipe.preparo = payload["preparo"]
    recipe.save()


def delete_recipe(id: int) -> None:
    recipe = find_recipe(id)
    recipe.delete()