'''Utilizando os conhecimentos adquiridos nas aulas anteriores onde foram feitos códigos estruturados, estamos incrementando o Python funcional. crie um projeto com o nome Calculadora python, depois crie um documento chamado controller dentro deste documento deve conter 4 funções com as operações básicas matemáticas. crie um outro documento chamado main, este documento deve estar importando as 4 operações matemáticas. crie uma função print solicitando dados ao usuário esta funcao deve ser com tipo predefinido tipo flutuante. deve ser utilizado o conceito de interpolação para criar um cabeçalho de um menu, dentro deste menu deve conter a possibilidade de fazer a impressão dos dados inseridos pelo usuário, permitindo assim o usuário escolher uma das 4 operações matemáticas importadas, consequentemente imprimindo assim o resultado desejado dos dados inseridos.'''

from time import sleep
import controller

while True:
    try:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        while True:  
                try:
                    print('-='*5, 'CALCULADORA', '-=' * 5)
                    opcao = int(input('''Digite uma das opções abaixo:\n1 - Soma\n2 - Subtrair\n3 - Multiplicação\n4 - Divisão\n5 - Digitar novos números\n6 - Sair\nQual opção? '''))
                    if opcao == 1:
                        somar = controller.soma(n1, n2)
                        print(f'A soma entre {n1} e {n2} é {somar}\n')
                        sleep(1)

                    elif opcao == 2:
                        subtrair = controller.subtracao(n1, n2)
                        print(f'A subtracao entre {n1} e {n2} é {subtrair}\n')
                        sleep(1)

                    elif opcao == 3:
                        multiplicar = controller.multiplicacao(n1, n2)
                        print(f'A multiplicação entre {n1} e {n2} é {multiplicar}\n')
                        sleep(1)

                    elif opcao == 4:
                        dividir = controller.divisao(n1, n2)
                        print(f'A soma entre {n1} e {n2} é {dividir}\n')
                        sleep(1)

                    elif opcao == 5:
                        n1 = float(input('Digite um número: '))
                        n2 = float(input('Digite outro número: '))
                        continue

                    elif opcao == 6:
                        break
                    
                    else:
                        print('Não existe a opção digitada\n')
                        sleep(1)
                
                except(ValueError):
                    print('Digite um valor valido\n')
                    sleep(1)
                    continue

    except (ValueError):
        print('Digite um valor valido')
        sleep(1)
        continue
    
    break

print('-=' * 5, 'Calculadora Finalizada', '-=' * 5)
    
          

