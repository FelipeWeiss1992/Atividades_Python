from carro import Carro

carro1 = Carro('Volskwagen', 'Gol', 'Preto', 'Hatch')

carro2 = Carro('Honda', 'Civic', 'Prata', 'Sedan')

print(carro1)
print(carro2)
print()
print(carro1.get_marca(), '|',carro1.get_modelo(), '|', carro1.get_cor(), '|',carro1.get_categoria())
print(carro2.get_marca(), '|',carro2.get_modelo(), '|', carro2.get_cor(), '|',carro2.get_categoria())
print()