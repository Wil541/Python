''' 
Desafio
    Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
Entrada
    A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.
Saída
    Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor.

IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input("Digite a quantidade de testes que deseja realizar: \n"))

n = N

while(n > 0):
    ''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
    '''
    A = str(input("Digite um valor maior que zero para A: \n"))
    B = str(input("Digite um valor maior que zero para B: \n"))
    tamanho_A = len(A)
    tamanho_B = len(B)
    tamanho_AB = tamanho_A - tamanho_B


    if ((0 < tamanho_A < 1000) and (0 < tamanho_B < 1000) and (tamanho_AB >= 0)):
        
        contem_B_em_A = A.split(B)
        if contem_B_em_A[1] == "":
            print("encaixa")
        else:
            print("nao encaixa")

    else:
        print("nao encaixa")
        
    n -= 1
