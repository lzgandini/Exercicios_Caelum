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
    def __init__(self, nome, sobrenome, cpf, nome_completo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.nome_completo = nome_completo

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente  #agregação
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()  #composição

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        if valor <= self.saldo:
            self.saca(valor)
            destino.deposita(valor)
            print('Transferência efetuada com sucesso!\n')

            resposta = input('Deseja ver o seu saldo atual (sim/nao)? ')
            if resposta == 'sim':
                return self.extrato()
            elif resposta == 'nao':
                return 'Até mais!'
            else:
                return 'Resposta inválida'

        else:
            return 'Saldo insuficiente'

    def extrato(self):
        return 'Numero da conta: {}\nSaldo: R$ {}'.format(self.numero, self.saldo)
        #print('\nDADOS DO CLIENTE') #deve chamar outra classe
        #print('Nome completo: {}'.format(Cliente.nome_completo))
        #print('CPF: {}'.format(Cliente.cpf))
