    # WORDLISTS
    # Wordlists são arquivos contendo uma palavra por linha. São utilizados em ataques de força bruta como quebra de autenticação, pode ser usada para testar a autenticação e confidencialidade de um sistema


import itertools        # Importa a biblioteca itertools: responsável por fornecer condições para interações como permutação e combinação. Utilizaremos para gerar uma lista com vários caracteres diferentes e sem repetição de palavras

string = input("String a ser permutada: ")

#resultado = itertools.permutations('abcdef', 3)                # String a ser permutada, e quantas deles ira utilizar ao realizar a permutação
resultado = itertools.permutations(string, len(string))         # String a ser permutada, verifica a quantidade de caracteres para verificar todas permutações possíveis

for i in resultado:         # Para  cada caracter em resultado:
    print("". join(i))      # Gera sequencia possíveis com os caracteres/quantidade passado