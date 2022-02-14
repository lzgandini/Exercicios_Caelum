from conta import Conta, Cliente

cliente1 = Cliente('Ana', 'Calina', '111111111-11')
cliente2 = Cliente('Marcela', 'Oliveira', '222222222-22')

conta1 = Conta('1', cliente1.nome, 120.0)
conta2 = Conta('2', cliente2.nome, 300.0)

print(conta1.data_abertura)
