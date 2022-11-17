'''- Crie um documento com namespace main e realize a importação da classe Conta e realize a importação, também do nosso CRUD e suas funções.
Crie uma funcao menu 
Dentro do menu crie um objeto de conta
Através da variável referência do nosso objeto chame cada atributo interno da nossa classe  e atribua valores aos mesmos
- Chame a função create e salve os dados inseridos no nosso objeto no arquivo txt
- Crie uma variável lista_contas e atribua a função read
Crie um print para imprimir lista_contas 
Crie um for com uma  c, variável  esta percorrendo a nossa variável que recebeu a função read lista_contas, dentro desse for crie um print imprimindo a variável c'''

from model import Conta
from controller import create, read

conta = Conta()

conta.titular = 'Felipe'
conta.numero = 1214
conta.saldo = 5250

create(conta)

lista_contas = read()

print(lista_contas)


for c in lista_contas:
    print(c)
