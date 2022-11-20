from model.pessoaFisica import PessoaFisica
from model.conta import Conta

def create_psf(conta):
    contas = open ('Banco\pessoafisica.txt', 'a')
    contas.write(str(conta)+ '\n')
    contas.close

def read_psf():
    lista_contas = []
    contas = open('Banco\pessoafisica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        conta = PessoaFisica()

        conta.id = conta_objeto[0]
        conta.agencia = conta_objeto[1]
        conta.numero_agencia = conta_objeto[2]

        conta.titular = conta_objeto[3]
        conta.cpf = conta_objeto[4]
        conta.saldo_inicial = conta_objeto[5]

        lista_contas.append(conta)
        print(conta_objeto)

    contas.close()

    return lista_contas

def update_psf(conta_update:Conta):
    lista_contas = []
    contas = open('Banco\pessoafisica.txt', 'r')
    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')
        if conta_update.id == int(conta_objeto[0]):
            lista_contas.append(str(conta_update) + '\n')
        else:
            lista_contas.append(conta)
            

    contas.close()
        
    contas = open('Banco\pessoafisica.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()

def delete_psf(id):
    lista_contas = []
    contas = open('Banco\pessoafisica.txt', 'r')
    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')
        if id != int(conta_objeto[0]):
            lista_contas.append(conta)

    contas.close()
        
    contas = open('Banco\pessoafisica.txt', 'w')
    contas.writelines(lista_contas)
    contas.close()

