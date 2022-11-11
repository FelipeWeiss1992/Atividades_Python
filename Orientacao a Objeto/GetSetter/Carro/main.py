from carro import Carro

def menu():
    
    carro = Carro(input('Digite a Marca:: '),
                  input('Digite o Modelo : '),
                  input('Digite a Cor : '),
                  input('Digita a categoria : '))
        
    return print(carro, '\n',f'O modelo é {carro.marca}, a marca é {carro.modelo}, a cor é {carro.cor}, e a categoria é {carro.categoria}')


while True:

    menu()

    resp = input('Deseja cadastrar outra pessoa: [S/N] ').strip().upper()
    if resp in 'N':
       break