from animal import Animal

animal1 = Animal('Cachorro', 'Rotweiler', 'Grande', 'Preto')
animal2 = Animal('Gato', 'Persa', 'Medio', 'Laranja')

print(animal1)
print(animal2)
print()
print(animal1.get_especie(), '|', animal1.get_raca(), '|', animal1.get_porte(), '|', animal1.get_cor())
print(animal2.get_especie(), '|', animal2.get_raca(), '|', animal2.get_porte(), '|', animal2.get_cor())
print()