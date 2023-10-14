menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else: 
            print("Valor informado é inválido!")

    if opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_lime = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não tem saldo suficiente!!!")

        if excedeu_lime:
            print("Atenção!!! O valor do saque excede o limite.")

        if excedeu_saques:
            print("Número máximo de saques diários excedido!")

        if valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque +=1

        else:
            print("O valor informado está inválido!")

    if opcao == "e":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:R$ {saldo: .2f}")
        print("===========================")

    elif opcao == "q":
        break

    else:
         print("Operação inválida, por favor selecione novamente a operação desejada.")