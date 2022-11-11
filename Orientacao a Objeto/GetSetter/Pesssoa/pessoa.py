'''utilizando o conhecimento adquirido crie um documento com namespace pessoa e nome da classe Pessoa, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, crie os seguintes atributos nome, cpf, idade, altura
Usando __  antes do nome do atributo, torne-os privados sendo assim  os mesmos serão acessíveis apenas na nossa classe.
Crie métodos set e get para cada atributo  da classe, lembrando que o método set é (definir), e o método get é (pegar), essa condicional é necessária devido os nossos atributos estarem privados.'''


class Pessoa:

    def __init__(self, nome, cpf, idade, altura):

        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def altura(self):
        return self.__altura 
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    

    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self.cpf} - Idade: {self.idade} - Altura: {self.altura}'