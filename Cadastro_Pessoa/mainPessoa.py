from controller2 import salvar, listar
from time import sleep

print('=' * 10,'Cadastro de nomes', '=' * 10)

while True:
    opcao = int(input('1 - Cadastrar Nomes\n2 - Listar Nomes\nQual opção:'))
    if opcao == 1:
        while True:
            nomes = salvar((input('Digite um nome:'))) 
            sleep(1)
            resp = str(input('Deseja cadastrar outro nome: [S/N]')).upper()
            if resp in 'S':
                continue
            else:
                break 

    elif opcao == 2:
        print('Lista de Nomes',listar())
        sleep(1)

    else:
        print('Nao existe a opção digitada')
        sleep(1)
    
    resp = str(input('Deseja continuar: [S/N]')).upper()
    if resp in 'S':
        continue
    else:
        break
