from produto import Produto

produto1 = Produto(input('ID: '), input('NomeProduto: '), input('Valor: '),input('qtd:'))

produto2 = Produto(input('ID: '), input('NomeProduto: '), input('Valor: '),input('qtd:'))

produto3 = Produto(input('ID: '), input('NomeProduto: '), input('Valor: '),input('qtd:'))

print('=-=' * 25)
print(produto1)
print((produto1).__init__)
print('=-=' * 25)
print(produto2)
print((produto2).__init__)
print('=-=' * 25)
print(produto3)
print((produto3).__init__)
print('=-=' * 25)