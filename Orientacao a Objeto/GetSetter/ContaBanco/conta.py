'''utilizando o conhecimento adquirido crie um documento com namespace conta e nome da classe Conta, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, crie os seguintes atributos titular, número, saldo, limite
Usando __  antes do nome do atributo, torne-os privados sendo assim  os mesmos serão acessíveis apenas na nossa classe.
Crie métodos set e get para cada atributo  da classe, lembrando que o método set é (definir), e o método get é (pegar), essa condicional é necessária devido os nossos atributos estarem privados.'''

class Conta:

    def __init__(self, titular, numero, saldo, limite):

        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    
    def set_titular(self, titular):
        self.__titular = titular
    def get_titular(self):
        return self.__titular

    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero

    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite 

    def __str__(self):
        return f'Titular: {self.get_titular()} - Numero: {self.get_numero()} - Saldo: R${self.get_saldo()} - Limite: R${self.get_limite()}'
        

        
