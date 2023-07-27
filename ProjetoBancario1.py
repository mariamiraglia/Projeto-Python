menu = '''
[d] Depositar  
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira o valor do depósito:"))

        if deposito > 0:
            saldo+=deposito
            extrato += f"Depósito:R${deposito:.2f}\n"
        else:
          print("Operação inválida: valor negativo.")
                   

    elif opcao == "s":
        saque = float(input("Insira o valor do saque:"))

        if saque > saldo:
          print("Operação inválida: sem saldo suficiente para saque.")

        elif saque > limite:
          print("Operação inválida: limite para saque excedido.")

        elif saque > 0:
          saldo-= saque
          extrato += f"Saque:R${saque:.2f}\n "
          numero_saques += 1

        elif numero_saques > limite_saques:
          print("Operação inválida: limite de saques excedidos.")

        else:
          print("Operação inválida.")



    elif opcao == "e":
        print("\n Extrato:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
    
    elif opcao == "q":
        break

    else: 
        print("Operação Inválida, por favor selecione novamente a operação desejada")
