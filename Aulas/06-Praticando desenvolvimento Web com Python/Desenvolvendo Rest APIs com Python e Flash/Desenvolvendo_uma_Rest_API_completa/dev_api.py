from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    # Lista/Dicionário
    {
    'id': '0',
    'nome': 'Willian',
    'habilidades': ['Python', 'Flask']
    },
    {
    'id': '1',
    'nome': 'Cardoso',
    'habilidades': ['Python', 'Django']}
]

# Devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor
# GET: recupera, PUT: vai permitir alterar, DELETE: deleta a id informada
@app.route('/dev/<int:id>/', methods=['GET','PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            # Posição do desenvolvedor dentro da biblioteca
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensgem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        # Retorna o que foi alterado
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        # Retorna o que foi alterado
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Excluido!!!'})

# Lista todos os desenvolvedores e permite geristrar novos desenvolvedores
# POST: vai permitir inserir, GET: recupera a id informada
@app.route('/dev/', methods=['POST', 'GET'])
def list_desenvlovedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        #return jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido'})
        return jsonify(desenvolvedores[posicao])
    # Consultar todos desenvolvedores
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
