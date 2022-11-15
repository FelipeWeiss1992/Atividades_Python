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
    def titular_conta(self):
        return self.__titular

    @titular_conta.setter
    def titular_conta(self, titular):
        self.__titular = titular
    
    @property
    def numero_cpf(self):
        return self.__cpf

    @numero_cpf.setter
    def numero_cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def saldo_inicial_conta(self):
        return self.__saldo_inicial

    @saldo_inicial_conta.setter
    def saldo_inicial_conta(self, saldo):
        self.__saldo_inicial = saldo  

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'{super().__str__()} - Titular: {self.titular_conta} - CPF: {self.numero_cpf} - Saldo Inicial: {self.saldo_inicial_conta} - Segundo Titular: {self.segundo_titular}'