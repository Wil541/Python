# DESAFIO
# Fompos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para essa primeira versão do sistemas devemos implementar apenas 3 operações: depósito, saque e extrato.

# DEPÓSITO
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser  armazenados em uma variável e exibidos na operação de extrato.
# SAQUE
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
# EXTRATO
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.


menu = """
========================================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
========================================
Informe a operação desejada =>: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nInformar valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:     R$ {valor: .2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print(
                "\nNão foi possivel realizar o depósito! \nO valor informado é inválido.\n")

    elif opcao == "2":
        valor = float(input("\nInformar valor do saque: "))

        excedeu_saldo = (valor > saldo)
        excedeu_limite = (valor > limite)
        excedeu_saques = (numero_saques >= LIMITE_SAQUES)

        if excedeu_saldo:
            print("\nOperação falhou! \nVocê não possui saldo suficiente.\n")

        elif excedeu_limite:
            print("\nOperação falhou! \nVocê excedeu o limite permitido para saque.\n")

        elif excedeu_saques:
            print("\nOperação falhou! \nVocê excedeu o numero de saques diário.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:        R${valor: .2f}\n"
            print("Saque realizado com sucesso!")
            numero_saques += 1

        else:
            print("\nOperação falhou! \nO valor informado é inválido.\n")

    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n----------------------------------------")
        print(f"\nSaldo:        R${saldo: .2f}")
        print("========================================")

    elif opcao == "0":
        break

    else:
        print("\nOperação inválida, por favor tente novamente!\n")
