import os       # Importa a biblioteca os (Sistema Operacional)
import time     # Importa biblioteca time (Tempo)

with open("hosts.txt") as file:     # abre o arquivo hosts.txt
    dump = file.read()              # Lê o arquivo txt e salva na variável dump
    dump = dump.splitlines()        # Para que os arquivos em exibição no terminal fique em linhas separadas

    print(dump, "\n")               # Imprime os arquivos dump e da uma quebra de linha

    for ip in dump:
        print("Verificando o ip: ", ip)
        print("-" * 60)
        os.system('ping -n 2 {}' .format(ip))
        print("-" * 60)
        time.sleep(5)       # a cada ping aguarda 5s para ir para o próximo comando



