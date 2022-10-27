'''crie novo documento mainSalario Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais representando os 4 últimos salários de uma pessoa. crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, utilizando o conceito de polimorfismo e imprima a palavra, Calculadora no centro da sua aplicação console. utilizando o conceito de máscara de substituição imprima descritivamente cada salário e a soma entre os mesmos imprimindo o resultado final. Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, deve ser utilizado os caracteres especiais de quebra de linha e na impressão deve apresentar apenas duas casas após a vírgula imprima no final utilizando a variável de soma para imprimir o resultado final do seu exercício. no documento controller crie uma função para calcular a soma do salario'''

from controller import somasalario

salario1 = float(input('Digite seu 1° salário: R$ '))
salario2 = float(input('Digite seu 2° salário: R$ '))
salario3 = float(input('Digite seu 3° salário: R$ '))
salario4 = float(input('Digite seu 4° salário: R$ '))

print('-='*5, 'CALCULADORA', '-=' * 5)

print('''Primeiro Salário : R${:.2f}\nSegundo Salário : R${:.2f}\nTerceiro Salário: R${:.2f}\nQuarto Salário: R${:.2f}\nA soma de todos os salários é R${:.2f}'''.format(salario1, salario2, salario3, salario4,somasalario(salario1,salario2,salario3,salario4)))
