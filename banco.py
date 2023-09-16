def menu():
    print('#####################')
    print('#########ATM#########')
    print('        Menu         ')
    print('1 - Depósito\n'
          '2 - Saque\n'
          '3 - Extrato\n'
          '4 - Novo Usuário\n'
          '5 - Nova Conta\n'
          '6 - Listar Contas\n'
          '0 - Sair\n')
    return int(input('Digite a opção desejada: '))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito:\tR$ {valor:.2f}')
        print()
        print('Depósito efetuado com sucesso.\n')
    else:
        print()
        print('Depósito não finalizado. Valor inválido.\n')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite_por_saque, total_de_saques, limite_de_saques):
    if total_de_saques < limite_de_saques:
        if valor > 0:
            if valor <= limite_por_saque:
                if saldo >= valor:
                    saldo -= valor
                    total_de_saques += 1
                    extrato.append(f'Saque:\tR$ {valor:.2f}')
                    print()
                    print("Saque realizado com sucesso.\n")
                else:
                    print()
                    print('Saldo insuficiente. Operação não realizada.\n')
            else:
                print()
                print(f'Saque não realizado. O valor solicitado excede o limite de R$ {limite_por_saque:.2f}\n')
        else:
            print()
            print('Saque não realizado. Valor inválido.\n')
    else:
        print()
        print('Desculpe, a solicitação excedeu o limite diário de saques.\n')
    return saldo, extrato, total_de_saques


def imprimir_extrato(saldo, /, *, extrato):
    print('##########EXTRATO##########')
    if len(extrato) > 0:
        [print(item) for item in extrato]
    else:
        print('Nenhuma operação realizada.')
    print(f'Saldo atual: R$ {saldo:.2f}')
    print('###########################\n')


def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente digitos): ")
    if not verifica_usuario_cadastrado(cpf, usuarios):
        nome = input("Digite o nome completo do usuário: ")
        data_de_nascimento = input("Digite a data de nascimento: (dd/mm/yyyy): ")
        endereco = input("Digite o endereço: (logradouro, nº, bairro, cidade, estado: ")
        usuario = {"cpf": cpf, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}
        usuarios.append(usuario)
        print("\nUsuário cadastrado com sucesso!\n")
    else:
        print("\nUsuário já cadastrado.\n")


def criar_conta(agencia, usuarios, numero_da_conta, contas):
    cpf = input("Digite o CPF (somente digitos): ")
    usuario = verifica_usuario_cadastrado(cpf, usuarios)
    if usuario:
        conta = {"agencia": agencia, "id_conta": numero_da_conta, "usuario": usuario}
        print()
        print("Conta criada com sucesso.\n")
        contas.append(conta)
        numero_da_conta += 1
    else:
        print()
        print("Usuário não encontrado. Conta não cadastrada.\n")
    return contas, numero_da_conta


def imprimir_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            print(f'Agência: {str(conta["agencia"]).zfill(4)}')
            print(f'Conta: {str(conta["id_conta"]).zfill(4)}')
            print(f'Titular: {conta["usuario"]["nome"]}\n')
    else:
        print('Nenhuma conta cadastrada.\n')


def verifica_usuario_cadastrado(cpf, usuarios):
    if len(usuarios) > 0:
        for usuario in usuarios:
            if cpf == usuario["cpf"]:
                return usuario


def main():
    # Valores iniciais da conta do usuário
    agencia = 1
    numero_da_conta = 1
    saldo = 0
    quantidade_de_saques = 0
    extrato = []
    usuarios = []
    contas = []
    limite_de_saques = 3
    limite_por_saque = 500

    while True:
        opcao = menu()
        print()

        if 0 <= opcao <= 6:
            if opcao == 1:
                valor = float(input('Digite o valor do depósito: R$ '))
                saldo, extrato = depositar(saldo, valor, extrato)
            elif opcao == 2:
                valor = float(input('Digite o valor do saque: R$ '))
                saldo, extrato, total_de_saques = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                                        limite_por_saque=limite_por_saque,
                                                        total_de_saques=quantidade_de_saques,
                                                        limite_de_saques=limite_de_saques)
            elif opcao == 3:
                imprimir_extrato(saldo, extrato=extrato)
            elif opcao == 4:
                criar_usuario(usuarios)
            elif opcao == 5:
                contas, numero_da_conta = criar_conta(agencia, usuarios, numero_da_conta, contas)
            elif opcao == 6:
                imprimir_contas(contas)
            else:
                print('Programa encerrado. Obrigado por utilizar nosso banco.')
                break
        else:
            print('Opção inválida.')


main()
