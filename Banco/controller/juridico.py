'''-na pasta controller crie um documento com name space juridico.py
- Realize a importação da classe from model.pessoaJuridica import PessoaJuridica
- Crie a  função create_pj recebendo um atributo interno create_pj (conta)
- Crie uma variável contas escrevendo no arquivo pessoajuridica.txt
- Chame essa variável, chamando a função interna do python que escreve .write()
- Coloque o atributo da função create_pj (conta) dentro de parênteses convertido para string.write(str(conta)) , faça com que cada dado inserido seja escrito na próxima linha utilizando quebra de linha, '\n'
- Escreva a função  interna contas.close() para fechar o arquivo'''

from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    contas = open ('Banco\pessoajuridica.txt', 'a')
    contas.write(str(conta)+ '\n')
    contas.close

'''-Crie a função read_pj()  dentro do bloco da função crie uma variável lista_contas recebendo uma lista vazia.
-Crie uma segunda variável contas abrindo nosso arquivo txt
-Crie um for com uma variável conta percorrendo a variável contas do arquivo pessoajuridica.txt
-faça novamente a variável do for conta e atribua a função interna do python Que retira os espaços .strip()
Crie uma variável conta_objeto recebendo a variável conta e utilize a função interna do python que identifica um índice na lista .split()
Crie um objeto de conta e chame cada atributo da nossa classe, inclusive os dados da classe base (Conta) agencia, numero_agencia, titular, cnpj e saldo_inicial.
E insira para cada atributo um índice da lista conforme a sequência de criação
Chame a variável criada inicialmente, lista_contas e recebendo a função interna do python .append()
Atribua à variável de referência do objeto
Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt'''

def read_pj():
    lista_contas = []
    contas = open('Banco\pessoajuridica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)
        conta = PessoaJuridica()
        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        lista_contas.append(conta)
    contas.close()

    return lista_contas