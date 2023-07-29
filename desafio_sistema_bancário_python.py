def mostrar_menu():
    menu = """

    [1] Cadastrar Usuário
    [2] Cadastrar Conta Corrente
    [3] Listar Contas
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [7] Sair

    => """

    return input((menu))

def depositar(saldo, valor, extrato, /):
    if(valor > 0):
        saldo += valor
        extrato += f"DEPÓSITO: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if(excedeu_saldo):
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif(excedeu_limite):
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif(excedeu_saques):
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif(valor > 0):
        saldo -= valor
        extrato += f"SAQUE: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSALDO:\t\tR$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = input("Insira o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios= []
    contas = []

    while(True):
        opcao = mostrar_menu()

        if(opcao == "4"):
            valor = float(input("Insira o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif(opcao == "5"):
            valor = float(input("Insira o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif(opcao == "6"):
            exibir_extrato(saldo, extrato=extrato)

        elif(opcao == "1"):
            cadastrar_usuario(usuarios)

        elif(opcao == "2"):
            numero_conta = len(contas) + 1
            conta = cadastrar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if(conta):
                contas.append(conta)
        
        elif(opcao == "3"):
            listar_contas(contas)

        elif(opcao == "7"):
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()