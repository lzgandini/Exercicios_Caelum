from conta import Conta, Cliente, Historico

cliente1 = Cliente('Ana', 'Borges', '111111111-11', 'Ana Borges')
cliente2 = Cliente('Marcela', 'Oliveira', '222222222-22', 'Marcela Oliveira')
cliente3 = Cliente('Ana', 'Madeira', '333333333-33', 'Ana Madeira')

conta1 = Conta('1', cliente1.nome_completo, 120.0)
conta2 = Conta('2', cliente2.nome_completo, 300.0)
conta3 = Conta('3', cliente3.nome_completo, 210.0)

conta1.saca(30.0)
conta2.transfere_para(conta3, 20.0)
conta1.deposita(200.0)
conta3.saca(300.0)
conta3.transfere_para(conta1, 500.0)

conta1.extrato()
conta1.historico.imprime()
conta2.extrato()
conta2.historico.imprime()
conta3.extrato()
conta3.historico.imprime()

