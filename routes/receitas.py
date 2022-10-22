from flask_restful import Resource


class Receita(Resource):
    def get(self, id):
        return {'msg': 'Teste'}

    def put(self, id):
        return {'msg': 'Teste'}

    def delete(self, id):
        return {'msg': 'Teste'}


class ListaReceita(Resource):
    def post(self):
        return {'msg': 'Teste'}

    def get(self):
        return {'msg': 'Teste'}


