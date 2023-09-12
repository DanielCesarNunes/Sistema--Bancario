# Valores iniciais da conta do usuário
saldo = 0.0
quantidade_de_saques = 0
extrato = []
LIMITE_DE_SAQUES = 3
LIMITE_POR_SAQUE = 500
total_de_saques = 0


while True:
    print('#####################')
    print('#########ATM#########')

    print('        Menu         ')
    print('1 - Depósito\n'
          '2 - Saque\n'
          '3 - Extrato\n'
          '0 - Sair\n')

    opcao = int(input('Digite a opção desejada: '))
    print()

    if 0 <= opcao <= 3:
        if opcao == 1:
            valor = float(input('Digite o valor do depósito: R$ '))
            if valor > 0:
                saldo += valor
                extrato.append(f'Depósito: R$ {valor:.2f}')
            else:
                print('Valor inválido.\n')
        elif opcao == 2:
            valor = float(input('Digite o valor do saque: R$ '))
            if total_de_saques < 3:
                if valor > 0:
                    if valor <= 500:
                        if saldo >= valor:
                            saldo -= valor
                            total_de_saques += 1
                            extrato.append(f'Saque: R$ {valor:.2f}')
                        else:
                            print('Saldo insuficiente. Operação não realizada.\n')
                    else:
                        print(f'Desculpe, o valor solicitado excede o limite de R$ {LIMITE_POR_SAQUE:.2f}\n')
                else:
                    print('Valor inválido.\n')
            else:
                print('Desculpe, a solicitação excedeu o limite diário de saques.\n')
        elif opcao == 3:
            print('##########EXTRATO##########')
            if len(extrato) > 0:
                [print(item) for item in extrato]
            else:
                print('Nenhuma operação realizada.')
            print('###########################\n')
            print(f'Saldo atual: R$ {saldo:.2f}\n')
        else:
            print('Programa encerrado. Obrigado por utilizar nosso banco.')
            break
    else:
        print('Opção inválida.')
