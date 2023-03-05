import os               # Importar a biblioteca os (integra os programas e recursos do S.O.)

print("#" * 60)         # Imprime "#" 60 vezes
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")    # Cria uma variável que vai receber do usuário um Ip
print("-" * 60)         # Imprime "-" 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host))                    # Camando o módulo system da biblioteca os - (chamando o comando ping com o numero de pacotes (-n -"num" {}) num = numero de pacotes = 6 {}) 
print("-" * 60)         # Imprime "-" 60 vezes