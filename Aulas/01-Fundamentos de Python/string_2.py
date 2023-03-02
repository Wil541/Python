nome = "Willian"
idade = 31
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Willian", "idade": 31}                                        # Dicionário para ser chamado posteriormente no código

print("Nome: %s Idade: %d" % (nome, idade))                                     # Formato não utilizado 

print("Nome: {} Idade: {}".format(nome, idade))                                 # Necessário colocar em ordem as variáveis

print("Nome: {1} Idade: {0}" .format(idade, nome))                              # pode chamar as posições da variável conforme foi informado em format
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))                # Pode chamar varias vezes as posições da variável conforme foi informado em format
print("Nome: {name} Idade: {age} {name} {age}" .format(name=nome,age=idade))    # Chamar conforme foi declarado as variáveis
print("Nome: {nome} Idade: {idade} " .format(**dados))                          # Chama o dicionário conforme foram declarados


print((f"Nome: {nome} Idade: {idade}"))                                         # "f" informa que irá chamar as variaveis dentro de {}
print((f"Nome: {nome} Idade: {idade} Saldo: {saldo: 10.2f}"))                    # saldo informado com 10 casas(+ uma do espaçamento) sendo 2 delas depois da virgula(ponto)(      45.44)
print((f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}"))                      # caso não informado a qunatidade de casas ira inserir o numero intiro 