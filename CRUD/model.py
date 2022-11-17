class Conta:

    __titular = ''
    __agencia = 0
    __numero = 0
    __saldo = 0

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def __str__(self):
        return f'{self.titular}; {self.agencia}; {self.numero}; {self.saldo}'
    



