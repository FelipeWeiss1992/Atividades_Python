from conta import Conta

class PessoaJuridica(Conta):
    
    __segundo_titular = ''

    def __init__(self, titular, cnpj, saldo_inicial):
          
        super().__init__('1215','15458', 'Pessoa Juridica')  
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo_inicial = saldo_inicial
        print('Passando pelo contrutor pessoa fisica')
        

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'{super().__str__()} - Titular: {self.__titular} - CNPJ: {self.__cnpj} - Saldo Inicial: {self.__saldo_inicial} - Segundo Titular: {self.segundo_titular}'