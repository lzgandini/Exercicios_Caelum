import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('\nData de abertura da conta: {}'.format(self.data_abertura))
        print('Transações: ')
        for t in self.transacoes:
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
        self.historico.transacoes.append('Deposito de R$ {}'.format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return 'Saldo insuficiente'  #NÃO ESTÁ FUNCIONANDO ESTE RETORNO
        else:
            self.saldo -= valor
            self.historico.transacoes.append('Saque de R$ {}'.format(valor))

    def transfere_para(self, destino, valor):
        if valor <= self.saldo:
            self.saca(valor)
            destino.deposita(valor)
            self.historico.transacoes.append(
                'Transferência de R$ {} para a conta {}'.format(valor, destino.numero))
        else:
            return 'Saldo insuficiente'  #NÃO ESTÁ FUNCIONANDO ESTE RETORNO

    def extrato(self):
        print('\nNumero da conta: {}\nSaldo: R$ {}'.format(self.numero, self.saldo))
        self.historico.transacoes.append('Tirou extrato. Saldo de R$ {}'.format(self.saldo))

        print('\nDados do Cliente:') #deve chamar outra classe
        print('Nome completo: {}'.format(self.cliente))
        #print('CPF: {}'.format(Cliente.cpf)) #NAO ESTÁ FUNCIONANDO
        
