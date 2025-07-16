def menu():
    print("="*35)
    print("SISTEMA BANCÁRIO".center(35))
    print("=" * 35)
    print("1) Sacar")
    print("2) Depositar")
    print("3) Visualizar extrato")
    print("0) Sair")


def sistema():
    saldo = 0
    extrato = []
    limite_saque = 0

    while True:
        menu()
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("❌ Entrada inválida. Digite um número de 0 a 3.")
            continue

        if opcao == 0:
            print("Encerrando sistema.")
            break

        elif opcao == 1:
            if limite_saque >= 3:
                print("Limite de saque diário atingido, por favor volte amanhã.")
                break
            while True:
                saque = input("Digite o valor do saque: ")
                try:
                    saque = float(saque)

                    if saque <= 0:
                        print("❌ O valor precisa ser positivo.")
                    elif saque > saldo:
                        print("❌ Saldo insuficiente!")
                    elif saque > 500:
                        print("O limite por saque é de R$ 500.")
                    else:
                        saldo -= saque
                        extrato.append(f"Saque: -R${saque:.2f}")
                        print(f"✅ Saque de R${saque:.2f} realizado com sucesso.")
                        limite_saque += 1
                        break
                except ValueError:
                    print("❌ Entrada inválida. Digite um número.")

        elif opcao == 2:
            while True:
                deposito = input("Digite o valor do deposito: ")
                try:
                    deposito = float(deposito)
                    if deposito <= 0:
                        print("❌ O valor precisa ser positivo.")
                    else:
                        saldo += deposito
                        extrato.append(f"Deposito: +R${deposito:.2f}")
                        print(f"✅ Deposito de R${deposito:.2f} realizado com sucesso.")
                        break
                except ValueError:
                    print("❌ Entrada inválida. Digite um número.")

        elif opcao == 3:
            while True:
                if extrato:
                    for item in extrato:
                        print(item)
                    break
                else:
                    print("Nenhuma movimentação.")
                    print(f"Saldo atual: R${saldo:.2f}")
                    print("====================\n")
                    break

sistema()
