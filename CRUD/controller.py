'''Crie um documento chamado controller e crie as duas funções create e read 
- Crie a  função create recebendo um atributo 
- Crie uma variável escrevendo no arquivo txt
- Chame essa variável chamando a função interna do python que escreve .write
- Coloque o atributo da função dentro de parênteses convertido para string, faça com que cada dado inserido seja escrito na próxima linha utilizando quebra de linha.
- Escreva a função  interna .close, para fechar o arquivo'''


from model import Conta

def create(conta):
    contas = open ('CRUD\lista_contas.txt', 'a')
    contas.write(str(conta)+ '\n')
    contas.close


'''-Crie a função read  dentro do bloco da função crie uma variável lista_contas recebendo uma lista vazia.
-Crie uma segunda variável contas abrindo nosso arquivo txt
Crie um for com uma variável conta percorrendo a variável contas do arquivo txt .
faça novamente a variável do for conta e atribua a função interna do python Que retira os espaços .strip
Crie uma variável conta_objeto recebendo a variável Conta e utilize a função interna do python que identifica um índice na lista .strip()
Crie um objeto de conta e chame cada atributo da nossa classe titular número e saldo.
E insira para cada atributo um índice da lista
Chame a variável criada inicialmente lista_contas e recebendo a funcao interna do python .append()
Atribua a variável de referencia do objeto
Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt
.close()
'''

def read():
    lista_contas = []
    contas = open('CRUD\lista_contas.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(';')
        print(conta_objeto)
        conta = Conta()
        conta.titular = conta_objeto[0]
        conta.numero = conta_objeto[1]
        conta.saldo = conta_objeto[2]
        lista_contas.append(conta)  
    contas.close()

    return lista_contas


