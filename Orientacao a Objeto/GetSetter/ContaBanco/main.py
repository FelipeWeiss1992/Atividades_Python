from conta import Conta

def menu():
    
    conta = Conta(input('Digite seu Nome: '),
                  input('Digite o número da conta: '),
                  input('Digite o saldo: R$ '),
                  input('Digite o Limite: R$ '))
        
    return print(conta, '\n',f'O titular é {conta.titular}, numero da conta é {conta.numero}, saldo da conta é R${conta.saldo}, limite da conta é R${conta.limite}')


while True:

    menu()

    resp = input('Deseja cadastrar outra pessoa: [S/N] ').strip().upper()
    if resp in 'N':
       break
    

   
   

