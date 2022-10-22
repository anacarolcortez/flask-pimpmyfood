from flask import Flask, jsonify, request
import json
from data.receitas_cadastradas import lista

app = Flask(__name__)


@app.route("/receitas/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_data(id: int):
    if request.method == 'GET':
        resp = get_data(id)
        return jsonify(resp)
    elif request.method == 'PUT':
        put_data(id, json.loads(request.data))
        resp = get_data(id)
        return jsonify(resp)
    elif request.method == 'DELETE':
        delete_data(id)
        return jsonify({'status': 'OK', 'msg': 'Receita excluída com sucesso'})


@app.route("/receitas", methods=['POST'])
def post_recepie():
    req = json.loads(request.data)
    post_data(req)
    return jsonify(req)


@app.route("/receitas/lista", methods=['GET'])
def get_all():
    return jsonify(lista)


def get_data(id: int):
    for receita in lista:
        if receita["id"] == id:
            return receita
    return {'erro': 'receita não encontrada'}       


def put_data(id, data):
    for receita in lista:
        if receita["id"] == id:
            receita["titulo"] = data["titulo"]
            receita["ingredientes"] = data["ingredientes"]
            receita["preparo"] = data["preparo"]
            break


def post_data(data):
    id = len(lista)+1
    lista.append(
        {
            "id": id,
            "titulo": data["titulo"],
            "ingredientes": data["ingredientes"],
            "preparo": data["preparo"]
        }
    )


def delete_data(id):
    for receita in lista:
        if receita["id"] == id:
            lista.remove(receita)



if __name__ == "__main__":
    app.run(debug=True)