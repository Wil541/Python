'''
OBJETIVO GERAL: Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

DESAFIO: Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário).

SEPARAÇÃO EM FUNÇÕES: Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você de forma que achar melhor.

SAQUE: A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

DEPÓSITO: A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

EXTRATO: A função extrato deve receber os argumentos apenas por posição e nome (positional only e keyword only). Argumentos posicionais: saldo; argumentos nomeados: extrato.

NOVAS FUÇÕES: Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

CRIAR USUÁRIO (cliente): O programa deve armazanar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: Logadouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

CRIAR CONTA CORRENTE: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O númeor da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

DICA: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

'''
import textwrap


def menu():
    # Menu principal do sistema
    menu = """\n
    ========================================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
    ========================================
    Informe a operação desejada =>: """

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    # Função para realizar um depósito na conta
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito:\tR$ {valor:.2f}")
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Função para realizar um saque na conta
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n @@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n @@@ Operação falhou! O valor do saque excedeu o limite. @@@")

    elif excedeu_saques:
        print("\n @@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")

    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    # Função para exibir o extrato da conta
    print("\n ========== EXTRATO ==========")
    print("Não houve movimentação até o momento!" if not extrato else '\n'.join(extrato))
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("================================")


def criar_usuario(usuarios):
    # Função para criar um novo usuário
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    # Função para filtrar um usuário por CPF
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    # Função para criar uma nova conta
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    # Função para listar as contas cadastradas
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\nInformar valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("\nInformar valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")


main()