menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        deposito = float(input("Valor que deseja depositar:"))

        if deposito <= 0:
            print("Valor inválido.")
            continue

        deposito_formatado = "Depósito"
        deposito_formatado = deposito_formatado.ljust(10)

        linha_extrato = f"{deposito_formatado}: R${deposito:10.2f}\n"
        extrato += linha_extrato

        saldo += deposito

    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingida.")
            continue

        saque = float(input("Valor que deseja sacar:"))

        if saque > LIMITE_SAQUE:
            print("Saque deve ser de até R$500,00.")
            continue

        if saque > saldo:
            print("Saldo insuficiente.")
            continue

        if saque <= 0:
            print("Valor inválido.")
            continue

        saque_formatado = "Saque"
        saque_formatado = saque_formatado.ljust(10)

        linha_extrato = f"{saque_formatado}: R${saque:10.2f}\n"
        extrato += linha_extrato

        saldo -= saque

        numero_saques += 1

    elif opcao == "e":
        print("Extrato:\n")

        print(extrato)

        saldo_formatado = "Saldo"
        saldo_formatado = saldo_formatado.ljust(10)
        print(f"{saldo_formatado}: R${saldo:10.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
