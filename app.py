from flask import Flask
from flask_restful import Api
from routes.receitas import Receita, ListaReceita


app = Flask(__name__)
api = Api(app)

api.add_resource(Receita, '/receitas/<int:id>')
api.add_resource(ListaReceita, '/receitas')

if __name__ == '__main__':
    app.run(debug=True)
