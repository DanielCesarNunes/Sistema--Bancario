class Conta:

    def __init__(self, id_conta, titular, saldo=0.0):
        self._agencia = 1
        self._conta = id_conta
        self._titular = titular
        self._saldo = saldo
        self._extrato = []

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def endereco(self):
        return self._titular.endereco

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._extrato.append(f'Depósito: R$ {valor:.2f}')
            print()
            print("Depósito realizado com sucesso.\n")
        else:
            print("Valor inválido. Depósito não efetuado.")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print()
                print("Saque realizado com sucesso.\n")
                self._extrato.append(f'Saque: R$ {valor:.2f}')
            else:
                print()
                print('Saldo insuficiente. Operação não realizada.\n')
        else:
            print()
            print(' Valor inválido. Saque não realizado.\n')

    def imprime_extrato(self):
        for transacao in self._extrato:
            print(transacao)

    def __str__(self):
        return f'Agência: {str(self._agencia).zfill(4)}\n'\
               f'Conta: {str(self._conta).zfill(4)}\n'\
               f'Titular: {self._titular.endereco}\n'

    @classmethod
    def criar_conta(cls, id_conta, titular):
        return cls(id_conta, titular)


class ContaCorrente(Conta):

    def __init__(self, id_conta, titular, limite_por_saque=500.0, limite_de_saques_diarios=3):
        super().__init__(id_conta, titular)
        self._titular = titular
        self._limite_por_saque = limite_por_saque
        self._limite_de_saques_diarios = limite_de_saques_diarios
        self._numero_de_saques = 0

    @property
    def nome(self):
        return self._titular.nome

    def sacar(self, valor):
        if self._numero_de_saques >= self._limite_de_saques_diarios:
            print('\nDesculpe, a solicitação excedeu o limite diário de saques. Saque não realizado.\n')
        elif valor > self._limite_por_saque:
            print(f'\nSaque não realizado. O valor solicitado excede o limite de R$ {self._limite_por_saque:.2f}\n')
        else:
            self._numero_de_saques += 1
            super().sacar(valor)

    def __str__(self):
        return f'Agência: {str(self.agencia).zfill(4)}\n'\
               f'Conta: {str(self.conta).zfill(4)}\n'\
               f'Titular: {self._titular.nome}\n'
