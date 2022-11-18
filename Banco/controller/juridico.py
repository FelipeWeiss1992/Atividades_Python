from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    contas = open ('Banco\pessoajuridica.txt', 'a')
    contas.write(str(conta)+ '\n')
    contas.close

def read_pj():
    lista_contas = []
    contas = open('Banco\pessoajuridica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        conta = PessoaJuridica()

        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]

        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        
        lista_contas.append(conta)
        print(conta_objeto)
    
    contas.close()

    return lista_contas