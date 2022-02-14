import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('Data de abertura da conta: {}'.format(self.data_abertura))
        print('Transações: ')
        for t in seld.transacoes:
            print('-', t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)

    def extrato(self):
        print('Numero da conta: {}\nSaldo: R$ {}'.format(self.numero, self.saldo))
        print('\nDADOS DO CLIENTE')
        #print('Nome: {} {}'.format(Cliente.nome, Cliente.sobrenome))
        #print('CPF: {}'.format(Cliente.cpf))
