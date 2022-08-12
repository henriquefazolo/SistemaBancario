from abc import ABC, abstractmethod


class Agencia:
    def __init__(self):
        self.__contas = []

    @property
    def contas(self):
        return self.__contas

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def fechar_conta(self, agencia=None, numero=None, cpf=None):
        for i in self.__contas:
            if str(agencia) and str(numero) in str(i):
                self.__contas.remove(i)
            elif str(cpf) in str(i):
                self.__contas.remove(i)
            else:
                return print('Conta não localizada')

        return print('Conta fechada com sucesso')


class Conta(ABC):
    @abstractmethod
    def __init__(self):
        self.__agencia = int()
        self.__numero = int()
        self.__nome = str()
        self.__cpf = str()
        self.__valor = float()

    def __str__(self):
        return f'{self.agencia}-{self.numero}-{self.nome}-{self.cpf}'

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()

    def transferir(self, valor, conta_destino):
        if self.valor >= valor:
            conta_destino.valor += valor
            self.valor -= valor
            return print(f'Valor {valor:.2f} transferido para {conta_destino}\n'
                         f'Seu saldo é de {self.valor:.2f}')
        else:
            return print('Saldo insuficiente')


class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__()
        self.__juros = float()

    @property
    def juros(self):
        return self.__juros

    @juros.setter
    def juros(self, percentual):
        self.__juros = percentual

    def render(self, meses):
        self.valor += self.valor * self.juros * meses
        return


class ContaCorrenteEspecial(ContaCorrente):
    def __init__(self):
        super().__init__()
        self.__limite_cheque_especial = float()

    @property
    def limite_cheque_especial(self):
        return self.__limite_cheque_especial

    @limite_cheque_especial.setter
    def limite_cheque_especial(self, limite):
        self.__limite_cheque_especial = limite

    def transferir(self, valor, conta_destino):
        if (self.valor + self.limite_cheque_especial) >= valor:
            conta_destino.valor += valor
            self.valor -= valor
            self.limite_cheque_especial += self.valor
            if self.valor <= 0:
                self.valor = 0
            return print(f'Valor {valor:.2f} transferido para {conta_destino}\n'
                         f'Seu saldo é de {self.valor:.2f}.\n'
                         f'Saldo Cheque Especial {self.limite_cheque_especial:.2f}.')
        else:
            return print('Saldo insuficiente')


# Criando agencia
agencia = Agencia()

# Criando contas
conta1 = ContaCorrente()
conta1.agencia = 3949
conta1.numero = 3653
conta1.cpf = '123.456.789-01'
conta1.nome = 'Henrique Fazolo'
conta1.valor = 1000

conta2 = ContaCorrente()
conta2.agencia = 1234
conta2.numero = 1234
conta2.cpf = '12345678910'
conta2.nome = 'Chico Bento'
conta2.valor = 0

conta3 = ContaCorrenteEspecial()
conta3.agencia = 1234
conta3.numero = 3214
conta3.cpf = '85214796315'
conta3.nome = 'Roberto Carlos'
conta3.valor = 500
conta3.limite_cheque_especial = 100

conta4 = ContaPoupanca()
conta4.agencia = 1234
conta4.numero = 3257
conta4.cpf = '14785214789'
conta4.valor = 100
conta4.juros = 0.05


# Adicionando Conta na agencia

agencia.adicionar_conta(conta1)
agencia.adicionar_conta(conta2)
agencia.adicionar_conta(conta3)
agencia.adicionar_conta(conta4)

# Operações

agencia.fechar_conta('3949', '3653')
conta3.transferir(530, conta2)
print(conta4.valor)
conta4.render(5)
print(conta4.valor)
