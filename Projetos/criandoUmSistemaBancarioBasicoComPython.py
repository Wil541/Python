# DESAFIO
# Fompos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para essa primeira versão do sistemas devemos implementar apenas 3 operações: depósito, saque e extrato.

# DEPÓSITO
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser  armazenados em uma variável e exibidos na operação de extrato.
# SAQUE
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
# EXTRATO
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.


# Apresenta todas as opções de transações para o usuário
menu = """
========================================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
========================================
Informe a operação desejada =>: """

saldo = 0               # Inicia com a conta zerada
limite = 500            # Limite para saque
extrato = ""            # Local onde ira salvar as informações de transações
numero_saques = 0       # Inicia o numero de saques zerado
# variável com letra maiuscula indica que é uma constante que não irá mudar limitando os saques a 3
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)     # lê a informação inserida pelo usuário

    if opcao == "1":        # se opção 1 DEPOSITO
        valor = float(input("\nInformar valor do depósito: "))

        if valor > 0:       # se valor positivo
            saldo += valor  # acrescenta valor no saldo
            # Acrescenta a informação em extrato
            extrato += f"Depósito:     R$ {valor: .2f}\n"
            # Informação para o usuário
            print("Depósito realizado com sucesso!")

        else:
            # Caso não for digitado uma informação aceitável levando em consideração que o usário so terá acesso a um teclado numérico
            print(
                "\nNão foi possivel realizar o depósito! \nO valor informado é inválido.\n")

    elif opcao == "2":      # se opção 2 SAQUE
        valor = float(input("\nInformar valor do saque: "))

        # Caso o valor desejado para saque seja maior que o saldo
        excedeu_saldo = (valor > saldo)
        # Caso o valor desejado para saque excedeu o Limite
        excedeu_limite = (valor > limite)
        # Caso a quantidade de saques execedeu o limite
        excedeu_saques = (numero_saques >= LIMITE_SAQUES)

        if excedeu_saldo:
            # Informação para o usuário caso excedeu saldo
            print("\nOperação falhou! \nVocê não possui saldo suficiente.\n")

        elif excedeu_limite:
            # Informação para o usuário caso excedeu limite
            print("\nOperação falhou! \nVocê excedeu o limite permitido para saque.\n")

        elif excedeu_saques:
            # Informação para o usuário caso excedeu numero de saques
            print("\nOperação falhou! \nVocê excedeu o numero de saques diário.\n")

        elif valor > 0:     # se valor positivo e passou njas outras condições
            saldo -= valor  # subtrai o valor do saque de saldo
            # Acrescenta a informação em extrato
            extrato += f"Saque:        R${valor: .2f}\n"
            # Informação para o usuário
            print("Saque realizado com sucesso!")
            # Acrescenta 1 na contagem de saques
            numero_saques += 1

        else:
            # Informação para o usuário
            print("\nOperação falhou! \nO valor informado é inválido.\n")

    elif opcao == "3":      # Se opção 3  EXTRATO
        print("\n=============== EXTRATO ===============")
        # Caso não tenha realizado nenhuma transação se não apresenta todas informações salvas
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n----------------------------------------")
        print(f"\nSaldo:        R${saldo: .2f}")
        print("========================================")

    elif opcao == "0":      # Se opção 3 SAI do sistema
        break

    else:
        # caso não for digitado nenhuma das opção apresentadas
        print("\nOperação inválida, por favor tente novamente!\n")
