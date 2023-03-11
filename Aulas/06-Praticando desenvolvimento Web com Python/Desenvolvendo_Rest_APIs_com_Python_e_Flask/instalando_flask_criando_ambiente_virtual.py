from flask import Flask
app = Flask (__name__)

@app.route("/<numero>", methods=['GET', 'POST'])        # <nemero>: parametro atravez da URI, GET: solicita do servidor, POST: envia para o servidor
def ola(numero):
    return 'Olá mundo.{}'. format(numero)

if __name__ == '__main__':
    app.run(debug=True)     # Irá rodar automaticamente após modificações (deixar apenas enquanto estiver em desenvolvimento)