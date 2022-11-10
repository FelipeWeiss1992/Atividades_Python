'''utilizando o conhecimento adquirido crie um documento com namespace carro e o nome da classe Carro, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, crie os seguintes atributos marca, modelo cor, categoria
Usando __  antes do nome do atributo, torne-os privados sendo assim  os mesmos serão acessíveis apenas na nossa classe.
Crie métodos set e get para cada atributo  da classe, lembrando que o método set é (definir), e o método get é (pegar), essa condicional é necessária devido os nossos atributos estarem privados.'''

class Carro:

    def __init__(self, marca, modelo, cor, categoria):

        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__categoria = categoria

    def set_marca(self, marca):
        self.__marca = marca
    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo
    def get_modelo(self):
        return self.__modelo   

    def set_cor(self, cor):
        self.__cor = cor
    def get_cor(self):
        return self.__cor  

    def set_categoria(self, categoria):
        self.__categoria = categoria
    def get_categoria(self):
        return self.__categoria     

    def __str__(self):
        return f'Marca: {self.__marca} - Modelo: {self.__modelo} - Cor: {self.__cor} - Marca: {self.__categoria}'