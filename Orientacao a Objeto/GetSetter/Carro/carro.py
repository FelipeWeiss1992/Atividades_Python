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

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo  
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
     
    @property
    def cor(self):
        return self.__cor 
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
   
    @property
    def categoria(self):
        return self.__categoria 
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
        

    def __str__(self):
        return f'Marca: {self.marca} - Modelo: {self.modelo} - Cor: {self.cor} - Marca: {self.categoria}'