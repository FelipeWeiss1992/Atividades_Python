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

    def set_especie(self, especie):
        self.__especie = especie
    def get_especie(self):
        return self.__especie

    def set_raca(self, raca):
        self.__raca = raca
    def get_raca(self):
        return self.__raca

    def set_porte(self, porte):
        self.__porte = porte
    def get_porte(self):
        return self.__porte

    def set_cor(self, cor):
        self.__cor = cor
    def get_cor(self):
        return self.__cor

    def __str__(self):
        return f'Especie: {self.__especie} - Raça: {self.__raca} - Porte: {self.__porte} - Cor: {self.__cor}'
        