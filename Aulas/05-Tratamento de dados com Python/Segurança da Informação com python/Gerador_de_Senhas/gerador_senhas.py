    # BIBLIOTECA RANDOM
    # Esta biblioteca interpreta geradores de números pseudoaleatórios para várias distribuições
    # Esta biblioteca será utilizada para randomizar letras e numeros, e a cada execução do programa gerar uma nova senha aleatória


import random       # Importa biblioteca random
import string

tamanho = int(input("Digite o tamanho de senha que voce deseja: ") )                    # Tamanho da senha desejada pelo usuário int pois é necessário ser um inteiro

chars = string.ascii_letters + string.digits + "ç!@#$%&*()-+=,.;:/?"                    # Estrutura da senha que será gerado (letters = maiuscula + minuscula, digts =0 até 9, e os caracteres desejados)

rnd = random.SystemRandom()                                                             # Biblioteca os classe urandom (os.urandom) gera números aleatórios

print("Sua senha segura é: " + "".join(rnd.choice(chars) for i in range(tamanho))       # Reto'rana a senha com a lista de caracteres randômico
