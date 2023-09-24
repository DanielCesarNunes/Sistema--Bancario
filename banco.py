from models.cliente import ClientePessoaFisica
from models.conta import ContaCorrente


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


def depositar(contas):
    id_conta = int(input("Digite o número da conta de depósito: "))
    conta = buscar_conta(id_conta, contas)
    if conta:
        print()
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)
    else:
        print()
        print('Conta não encontrada.\n')


def sacar(contas):
    id_conta = int(input("Digite o número da conta: "))
    conta = buscar_conta(id_conta, contas)
    if conta:
        print()
        valor = float(input("Informe o valor do saque: "))
        conta.sacar(valor)
    else:
        print()
        print('Conta não encontrada.\n')


def imprimir_extrato(contas):
    id_conta = int(input("Digite o número da conta: "))
    conta = buscar_conta(id_conta, contas)
    if conta:
        print('\n##########EXTRATO##########')
        conta.imprime_extrato()
        print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
        print("==========================================")
    else:
        print()
        print("Conta não encontrada.\n")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente digitos): ")
    if not buscar_usuario(cpf, usuarios):
        print()
        nome = input("Digite o nome completo do usuário: ")
        print()
        data_de_nascimento = input("Digite a data de nascimento: (dd/mm/yyyy): ")
        print()
        endereco = input("Digite o endereço: (logradouro, nº, bairro, cidade, estado: ")
        cliente = ClientePessoaFisica(nome, data_de_nascimento, cpf, endereco)
        usuarios.append(cliente)
        print("\nCliente cadastrado com sucesso!\n")
    else:
        print("\nUsuário já cadastrado.\n")
    return usuarios


def criar_conta(numero_da_conta, usuarios, contas):
    cpf = input("Digite o CPF (somente digitos): ")
    usuario = buscar_usuario(cpf, usuarios)
    if usuario:
        conta = ContaCorrente.criar_conta(numero_da_conta, usuario)
        print()
        print("Conta criada com sucesso.\n")
        contas.append(conta)
    else:
        print()
        print("Cliente não encontrado. Conta não cadastrada.\n")
    return contas


def imprimir_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            print(conta)
    else:
        print('Nenhuma conta cadastrada.\n')


def buscar_conta(id_conta, contas):
    if len(contas) > 0:
        for conta in contas:
            if id_conta == conta.conta:
                return conta


def buscar_usuario(cpf, usuarios):
    if len(usuarios) > 0:
        for usuario in usuarios:
            if cpf == usuario.cpf:
                return usuario
        else:
            return None


def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        print()

        if 0 <= opcao <= 6:
            if opcao == 1:
                depositar(contas)
            elif opcao == 2:
                sacar(contas)
            elif opcao == 3:
                imprimir_extrato(contas)
            elif opcao == 4:
                usuarios = criar_usuario(usuarios)
            elif opcao == 5:
                id_conta = len(contas) + 1
                contas = criar_conta(id_conta, usuarios, contas)
            elif opcao == 6:
                imprimir_contas(contas)
            else:
                print('Programa encerrado. Obrigado por utilizar nosso banco.')
                break
        else:
            print('Opção inválida.')


main()
