'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns
   casos, é necessário converter/tratar os dados de entrada;
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a
   impressão dos dados de saída.
'''
T = int(input("Digite a quantidade de testes: "))

for i in range(T):

     N = int(input("Digite quantos refrigerante vai comprar: "))
     K = int(input("Digite o numero de garrafas vazias para trocar por uma cheia: "))

     if (N > K):

          garrafas_cheias = int(N/K)
          qtd_trocada = (garrafas_cheias * K)
          total_garrafas = (N - qtd_trocada) + garrafas_cheias

          print(total_garrafas)

          i += 1

     else:

          total_garrafas = N

          print(total_garrafas)

          i += 1


'''
T = int(input())         # Lê um número inteiro T da entrada padrão e atribui-o à variável T

for i in range(T):       # Para cada valor de i de 0 a T-1, faz o seguinte:
  
  N, K = map(int, input().split())      # Lê dois números inteiros N e K da entrada padrão e atribui-os às variáveis N e K usando a função map a função split é apenas para separa-las
  numero_garrafas = N % K + N / K       # Calcula o número de garrafas 
  print(int(numero_garrafas))           # Imprime o valor de numero_garrafas
