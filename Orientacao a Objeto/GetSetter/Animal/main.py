from animal import Animal

def menu():
    
    animal = Animal(input('Digite a Especie: '),
                  input('Digite a raça : '),
                  input('Digite o porte : '),
                  input('Digita a cor : '))
    
    return print(animal, '\n',f'A espécie é {animal.especie}, a raça é {animal.raca}, o porte é {animal.porte}, a cor é {animal.cor}')


    
menu()
