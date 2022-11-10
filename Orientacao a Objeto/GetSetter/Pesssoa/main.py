from pessoa import Pessoa

pessoa1 = Pessoa('Felipe', '854.584.098-85', 30, 1.81)

pessoa2 = Pessoa('Maiara', '458.768.787-88', 22, 1.61)


print(pessoa1)
print(pessoa2)
print()
print(pessoa1.get_nome(), '|',pessoa1.get_cpf(), '|',pessoa1.get_idade(), '|',pessoa1.get_altura())
print()
print(pessoa2.get_nome(), '|',pessoa2.get_cpf(), '|',pessoa2.get_idade(), '|',pessoa2.get_altura())
print()

