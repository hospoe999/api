from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
COURS(app)

@app.route("/api/saludar", methods=['POST'])
def saludar():
  data = request.get_json()
  nome = data.get("nome")
  if nome == "Elvis":
    return jsonify({"menssagem": f"ola {nome}"})
  else:
    return jsonify({"menssagem": "nome nao autorizado"}), 403
if __name__ == '__main__':
  app.run()
