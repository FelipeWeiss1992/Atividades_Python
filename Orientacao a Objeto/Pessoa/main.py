from pessoa import Pessoa

pessoa1 = Pessoa(input('Nome: '), input('sobreNome: '), input('Idade: '),input('CPF:'))

pessoa2 = Pessoa(input('Nome: '), input('sobreNome: '), input('Idade: '),input('CPF:'))

pessoa3 = Pessoa(input('Nome: '), input('sobreNome: '), input('Idade: '),input('CPF:'))

print('=-=' * 25)
print(pessoa1)
print((pessoa1).__init__)
print('=-=' * 25)
print(pessoa2)
print((pessoa2).__init__)
print('=-=' * 25)
print(pessoa3)
print((pessoa3).__init__)
print('=-=' * 25)