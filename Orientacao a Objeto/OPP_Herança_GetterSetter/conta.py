class Conta:

    def __init__(self, agencia, numero, tipo):

        self.__agencia = agencia
        self.__numero = numero
        self.__tipo = tipo
        print('Passando pelo contrutor Conta')

    @property
    def agencia_conta(self):
        return self.__agencia

    @agencia_conta.setter
    def agencia_conta(self, agencia):
        self.__agencia = agencia

    @property
    def numero_conta(self):
        return self.__numero

    @numero_conta.setter
    def numero_conta(self, numero):
        self.__agencia = numero

    @property
    def tipo_conta(self):
        return self.__tipo

    @tipo_conta.setter
    def tipo_conta(self, tipo):
        self.__tipo = tipo    

    @property
    def segundo_titular(self):
        return self.__segundo_titular
        
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular    

    def __str__(self):

        return f'Agencia: {self.agencia_conta} - Numero: {self.numero_conta} - Tipo: {self.tipo_conta}'