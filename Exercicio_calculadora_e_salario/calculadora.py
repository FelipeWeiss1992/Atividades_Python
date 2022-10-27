from controller import soma,subtracao,divisao,multiplicacao

opcao = 0

def menu():
    print('-'* 25, 'menu', '-' * 25)

    cond = 'sim'
    while cond == 'sim':
        n1 = int(input('Digite primeiro número:'))
        n2 = int(input('Digite segundo número:'))

        opcao = int(input('Digite uma das opções abaixo:\n1 - Somar\n2 - subtrair\n3 - divisão\n4 - multiplicar\nQual opção:'))
        
        match opcao:
            case 1:
                print(f'A soma dos números digitados é {soma(n1,n2)}')

            case 2:
                print(f'A subtracao dos números digitados é {subtracao(n1,n2)}')

            case 3:
                print(f'A divisao dos números digitados é {divisao(n1,n2)}')

            case 4:
                print(f'A multiplicao dos numeros digitados é {multiplicacao(n1,n2)}')

            case _:
                print('Digite uma opção valida')

        cond = str(input('Deseja continuar: sim ou nao \n:>'))
            
menu()       