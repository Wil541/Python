    # PROTOCOLO TCP:
    # "Protocolo de Controle de Transmissão (do inglês: Transmission Control Protocol, abreviado TCP) é um dos protocolos de comunicação, da camada de transporte da rede de computadores do Modelo OSI, que dão suporte a rede global Internet, verificando se os dados são enviados na sequência correta e sem erros via rede."

    # Nosso programa verificará se os dados são enviados de maneira íntegra



import socket       # Relacionamento entre a placa de rede e o Sistema Operacional
import sys          # Fornece o acesso a algumas variáveis/funçoes com forte interação com o interpretador Python

def main():         # Função principal main
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0) # Objeto de conexão
    except socket.error as erro:
        print("A conexão falhou!!!")
        print("Erro: {}".format(erro))      # Exibe o formato do erro encontrado
        sys.exit()                          # Caso erro irá sair da aplicação

    print("Socket criado com sucesso!")

    hostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    portaAlvo = input("Digite a Porta a ser conectada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))       #segundo argumento não aceita String, por este motivo transformou em inteiro
        print("Clinte TCP conectado com Sucesso no Host: " + hostAlvo + " e na Porta: " + portaAlvo)
        s.shutdown(2)                               # Desligar o o bjeto de conexão para não ficar em loop

    except socket.error as erro:
        print("Não foi possivel conectar no Host: " + hostAlvo + " e na Porta: " + portaAlvo)
        print("Erro: {}".format(erro))      # Exibe o formato do erro encontrado
        sys.exit()                          # Caso erro irá sair da aplicação

if __name__ == "__main__":      # se o nome da função for main, chamar a função main
    main()