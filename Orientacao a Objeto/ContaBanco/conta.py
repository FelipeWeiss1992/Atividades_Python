'''utilizando o conhecimento adquirido crie um documento com namespace e nome da classe, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, crie os seguintes atributos titular, número, saldo, limite
Crie um método encapsulando o extrato de uma conta, o extrato deve imprimir o número da conta, o nome do titular e o saldo inicial depositado.
Crie um método depositar, utilizando o atributo específico do método (valor), no encapsulamento acesse os atributos da classe e utilizando os operadores relacionais de incremento receba o  atributo do método em questão e retorne o mesmo.'''


class Conta:

    def __init__(self, titular, numero, saldo, limite):
        
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def extrato(self):

        return f'O saldo da conta {self.numero} do {self.titular} é {self.saldo}'

    def depositar(self, valor):

        self.saldo += valor
        
        return valor

    def sacar(self, valor):

        if self.saldo - valor < valor:
            print('Não a saldo a sacar')

        else:
            self.saldo -= valor   


    def transferir(self, valor, destino):

        self.saldo -= valor
        destino.saldo += valor
        return valor