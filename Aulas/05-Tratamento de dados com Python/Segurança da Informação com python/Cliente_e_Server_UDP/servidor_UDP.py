    # Quando for executar o teste:
    # rodar primeiro o servidor e em seguida o cliente


import socket                                               # Relacionamento entre a placa de rede e o Sistema Operacional
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # Objeto de conexão (DGRAM = protocolo de datagrama do usuário)

print("Socket criado com Sucesso!")

host = "localhost"      # Rede local/interna da sua máquina
port = 5432             # Porta em que irá se conectar com o cliente

s.bind((host, port))                                # Irá realizar a ligação entre Cliente/Servidor
mensagem = "\nServidor: Olá cliente, tudo bem?"     # Mensagem para o cliente

while 1:
    dados, end = s.recvfrom(4096)                       # Vai receber/esperar resposta do cliente 4096 bytes e guardar em dados e end
    if dados:
        print("Servidor enviando mensagem...")          # Caso houver dados
        s.sendto(dados + (mensagem.encode()), end)      # Enviar mensagem via UDP dentro do pacote

