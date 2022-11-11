from pessoa import Pessoa

def menu():
    
    pessoa = Pessoa(input('Digite seu Nome: '),
                  input('Digite o CPF : '),
                  input('Digite o idade : '),
                  input('Digita a altura : '))
        
    return print(pessoa, '\n',f'O nome é {pessoa.nome}, seu CPF  é {pessoa.cpf}, sua idade é R${pessoa.idade}, sua altura é R${pessoa.altura}')

menu()

   

