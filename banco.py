menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! Valor de depósito inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        message = None
        if valor > saldo:
            message = "Operação falhou! Saldo insuficiente."
        if valor > limite:
            message = "Operação falhou! Valor do saque excede o limite por transação."
        if numero_saques >= LIMITE_SAQUES:
            message = "Operação falhou! Já realizou o máximo de saques diários "
        if valor <= 0:
            message = "Operação falhou! Foi informado um valor inválido"

        if message is None:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n "
            numero_saques = numero_saques + 1
            print(numero_saques)
            message = "Operação realizada com sucesso!"
        
        print(message)

    elif opcao == "e":
        
        extrato_alinhado = '\n'.join([' ' * 8 + linha.lstrip() for linha in extrato.splitlines()])
        exibe_extrato = f"""
        {"=" * 16} EXTRATO {"=" * 16}
        {"Não existem movimentações para o período" if not extrato else extrato_alinhado}
        Saldo: R$ {saldo:.2f}
        {"=" * 41}
        """

        print(exibe_extrato)
        
    elif opcao == "q":
        break
    
    else:
        print("Opção invalida!")
