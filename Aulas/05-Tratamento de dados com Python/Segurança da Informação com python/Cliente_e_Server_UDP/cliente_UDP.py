    # PROTOCOLO UDP:
    # "O UDP (User Datagram Protocol) ou Protocolo de Datagrama de Usuário é um protocolo simples da camada de transporte que permite que a aplicação envie um datagrama dentro num pacote IPv4 ou IPv6 a um destino, porem sem qualquer tipo de garantia que o pacote chegou corretamente"



import socket                                               # Relacionamento entre a placa de rede e o Sistema Operacional
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # Objeto de conexão (DGRAM = protocolo de datagrama do usuário)

print("Socket criado com Sucesso!")

host = "localhost"                          # Rede local/interna da sua máquina
porta = 5433                                # Porta em que irá se conectar com o servidor
mensagem = "Olá servidor, tudo certo?"      # Mensagem para o servidor

try:                                                # Tentar enviar/receber a mensagem
    print("\nCliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))       # Empacotando e enviando a mensagem com pacotes UDP para o servidor + host e porta em que irá se conectar

    dados, servidor = s.recvfrom(4096)              # Vai receber/esperar resposta do servidor 4096 bytes e guardar em dadoe e servidor
    dados = dados.decode()                          # Desempacotar os dados
    print("Cliente: " + dados)                      # O que enviou e o que o servidor recebeu

finally:
    print("Cliente: Fechando a Conexão")
    s.close()                                       # Fecha a conexão