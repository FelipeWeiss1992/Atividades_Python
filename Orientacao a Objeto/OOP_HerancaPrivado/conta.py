class Conta:
    def __init__(self, agencia, numero, tipo):

        self.__agencia = agencia
        self.__numero = numero
        self.__tipo = tipo

        print('Passando pelo contrutor da classe Conta')
        
    def __str__(self):

        return f'Agencia: {self.__agencia} - Numero: {self.__numero} - Tipo: {self.__tipo}'
        
        