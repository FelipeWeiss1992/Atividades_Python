class Conta:
    __id = 0
    __agencia = 'Blumenau'
    __numero_agencia = '0101'

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero_agencia(self):
        return self.__numero_agencia
    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        self.__numero_agencia = numero_agencia

    def __str__(self):
        return f'{self.id}; {self.agencia}; {self. numero_agencia}'