from flask import Flask, request, jsonify
from flask_cors import CORS  # Corrigido aqui

app = Flask(__name__)
CORS(app)  # Corrigido aqui

@app.route("/api/saludar", methods=['POST'])
def saludar():
    data = request.get_json()
    nome = data.get("nome")  # Corrigido aqui (confira se a chave é "nome" mesmo)
    if nome == "Elvis":
        return jsonify({"mensagem": f"ola {nome}"})  # Corrigido "menssagem" para "mensagem"
    else:
        return jsonify({"mensagem": "nome nao autorizado"}), 403  # Corrigido "menssagem"

if __name__ == '__main__':
    app.run()
