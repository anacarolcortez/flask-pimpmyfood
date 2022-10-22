from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Receita(Resource):
    def get(self, id):
        return {'msg': 'Teste'}

    def put(self, id):
        return {'msg': 'Teste'}

    def delete(self, id):
        return {'msg': 'Teste'}


api.add_resource(Receita, '/receitas/<id>')

if __name__ == '__main__':
    app.run(debug=True)
