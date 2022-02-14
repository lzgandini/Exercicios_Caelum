from conta import Conta, Cliente

cliente1 = Cliente('Ana', 'Calina', '111111111-11')
cliente2 = Cliente('Marcela', 'Oliveira', '222222222-22')
cliente3 = Cliente('Ana', 'Madeira', '333333333-33', 'Ana Madeira')

conta1 = Conta('1', cliente1.nome_completo, 120.0)
conta2 = Conta('2', cliente2.nome_completo, 300.0)
conta3 = Conta('3', cliente3.nome_completo, 210.0)

"""EXERCICIO N.12 (INCOMPLETO)
Dúvida: Modifique o método extrato() da classe Conta para imprimir, além do número e saldo, os dados do cliente."""

print('\nN. Conta: {}\nNome completo do titular: {}\nSaldo: {}'.format(conta1.numero, conta1.cliente, conta1.saldo))
print('\nN. Conta: {}\nNome completo do titular: {}\nSaldo: {}'.format(conta2.numero, conta2.cliente, conta2.saldo))
print('\nN. Conta: {}\nNome completo do titular: {}\nSaldo: {}'.format(conta3.numero, conta3.cliente, conta3.saldo))
