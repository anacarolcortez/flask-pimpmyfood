from flask import jsonify, request
from flask_restful import Resource, abort
from services import receitas
from utils import serializer as s
import json

class Receita(Resource):
    def get(self, id):
        try:
            response = receitas.find_recipe_by_id(id)
            return response
        except Exception:
            abort(404, message="Receita não encontrada")


    def put(self, id):
        try:
            data = s.recipe_put_args.parse_args()
            receitas.update_recipe(id, data)
            response = receitas.find_recipe_by_id(id)
            return response
        except Exception as e:
            abort(400, message="Erro ao editar receita")


    def delete(self, id):
        try:
            receitas.delete_recipe(id)
            return {'msg': 'Receita excluída com sucesso'}, 200
        except Exception:
            abort(400, message="Erro ao excluir receita")


class ListaReceita(Resource):
    def post(self):
        data = s.recipe_post_args.parse_args()
        receitas.create_recipe(data)
        resp = receitas.find_recipe_by_name(data["titulo"])
        return resp, 201

    def get(self):
        return receitas.find_all_recipes()


