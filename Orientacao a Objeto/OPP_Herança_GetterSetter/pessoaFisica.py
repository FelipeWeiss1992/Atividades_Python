from conta import Conta

class PessoaFisica(Conta):
    
    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
          
        super().__init__('1212','15435', 'Pessoa Fisica')  
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        print('Passando pelo contrutor pessoa fisica')
        
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular.title()
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial

    @saldo_inicial.setter
    def saldo_inicial(self, saldo):
        self.__saldo_inicial = saldo  


    def __str__(self):
        return f'{super().__str__()} - Titular: {self.titular_conta} - CPF: {self.numero_cpf} - Saldo Inicial: {self.saldo_inicial_conta} - Segundo Titular: {self.segundo_titular}'