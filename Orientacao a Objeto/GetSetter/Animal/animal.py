'''utilizando o conhecimento adquirido crie um documento com namespace animal e nome da classe Animal, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, crie os seguintes atributos espécie, raça, porte, cor
Usando __  antes do nome do atributo, torne-os privados sendo assim  os mesmos serão acessíveis apenas na nossa classe.
Crie métodos set e get para cada atributo  da classe, lembrando que o método set é (definir), e o método get é (pegar), essa condicional é necessária devido os nossos atributos estarem privados.'''

class Animal():

    def __init__(self, especie, raca, porte, cor):

        self.__especie = especie
        self.__raca = raca
        self.__porte = porte
        self.__cor = cor

    @property
    def especie(self, especie):
        self.__especie = especie
    @especie.getter
    def especie(self):
        return self.__especie

    @property
    def raca(self, raca):
        self.__raca = raca
    @raca.getter
    def raca(self):
        return self.__raca

    @property
    def porte(self, porte):
        self.__porte = porte
    @porte.getter
    def porte(self):
        return self.__porte

    @property
    def cor(self, cor):
        self.__cor = cor
    @cor.getter
    def cor(self):
        return self.__cor

    def __str__(self):
        return f'Especie: {self.especie} - Raça: {self.raca} - Porte: {self.porte} - Cor: {self.cor}'
        