''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''

a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':

        if c == 'carnivoro':
            print("aguia")

        elif c == 'onivoro':
            print("pomba")

    elif b == 'mamífero':

        if c == 'onivoro':
            print("homem")

        elif c == 'herbivoro':
            print("vaca")

elif a == 'invertebrado':
    if b == 'inseto':

        if c == 'hematofago':
            print("pulga")

        elif c == 'herbivoro':
            print("lagarta")

    elif b == 'anelideo':

        if c == 'hematofago':
            print("sanguessuga")

        elif c == 'onivoro':
            print("minhoca")
