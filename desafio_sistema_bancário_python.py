menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while(True):
    opcao = input(menu)

    if(opcao == "d"):
        valor_depositado = float(input("Insira o valor do depósito: "))

        if(valor_depositado > 0):
            saldo += valor_depositado
            extrato += f"DEPÓSITO: R$ {valor_depositado:.2f}\n"
        else:
            print("Apenas são permitidos depósitos de valores positivos, tente novamente.")

    elif(opcao == "s"):
        valor_saque = float(input("Insira o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if(excedeu_saldo):
            print("Saldo insuficiente.")
        elif(excedeu_limite):
            print("Valor do saque excede o limite.")
        elif(excedeu_saques):
            print("Número máximo de saques excedido.")
        elif(valor_saque > 0):
            saldo -= valor_saque
            extrato += f"SAQUE: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("Apenas são permitidos saques de valores positivos, tente novamente.")

    elif(opcao == "e"):
        print("\n############ EXTRATO ############")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        print("#################################")
    elif(opcao == "q"):
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")