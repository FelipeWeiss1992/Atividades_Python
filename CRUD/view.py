from random import randint
from model import Conta
from controller import create, read

def menu():

    conta = Conta()

    conta.titular = str(input('Digite Seu Nome Completo: '))
    conta.agencia = 2300
    conta.numero = randint(1, 999999)
    conta.saldo = 0

    create(conta)
    print('Conta Criada com Sucesso.')
    lista_contas = read()


menu()
