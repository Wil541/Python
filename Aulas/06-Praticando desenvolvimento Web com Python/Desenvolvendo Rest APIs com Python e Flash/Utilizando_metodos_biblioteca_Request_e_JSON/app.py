from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')    #  < > tipo e o parametro que input que ira receber casso diferente ira dar erro
def pessoa(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome': 'Rafael', 'profissao': 'Desenvolvedor'})      # Parametros que ira ser exibido

# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods = ['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)