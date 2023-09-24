class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @staticmethod
    def adicionar_conta(self, conta):
        self._contas.append(conta)


class ClientePessoaFisica(Cliente):
    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self._data_de_nascimento = data_de_nascimento

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
