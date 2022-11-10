'''-Crie um método str recebendo a variável de referência ao objeto, retorne com um f string, e atribua os métodos get de cada atributo privado da nossa classe. Crie um Documento  com namespace Main a partir do documento conta importe a classe Conta.
-Crie um objeto de conta e solicite ao usuário a atribuição de valores através de input para cada atributo do nosso construtor.
Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos get imprima os valores inseridos no nosso objeto, com um novo print realize a impressão de todos os valores dos nossos atributos. 
-Crie um novo objeto conta2 e solicite ao usuário a atribuição de valores, através de input para cada atributo do nosso construtor. 
Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos get imprima os valores inseridos no nosso objeto, com um novo print realize a impressão de todos os valores dos nossos atributos de conta2'''

from conta import Conta

conta1 = Conta('Felipe', 5258, 500, 1000)

conta2 = Conta('Maiara', 2356, 250, 500)

print(conta1)
print(conta2)
print()
print(conta1.get_titular(), '|', conta1.get_numero(), '|',conta1.get_saldo(), '|',conta1.get_limite())
print()
print(conta2.get_titular(), '|',conta2.get_numero(), '|',conta2.get_saldo(), '|',conta2.get_limite())
print()