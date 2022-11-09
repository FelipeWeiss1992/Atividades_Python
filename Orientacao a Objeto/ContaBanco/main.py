from conta import Conta

conta1 = Conta('Felipe', 12314, 1500, 2000)

conta2 = Conta('Maiara', 34556, 5000, 7000)

print('Extrato inicial')
print(conta1.extrato())
print(conta2.extrato())
print()
conta1.depositar(int(input('Digite o valor para depositar na conta do Felipe: R$ '))),'\n'

print(conta1.extrato())
print()
conta1.sacar(int(input('Digite o valor de Saque da conta do Felipe: R$ '))), '\n'

print(conta1.extrato())
print()
conta1.transferir(int(input('Digite o valor da Transferencia da conta do Felipe para Maiara: R$ ')),conta2)
print()

print(conta1.extrato())
print(conta2.extrato())



