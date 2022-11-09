#EXERCICIO-04 crie um documento instanciando uma classe chamada carro , crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor marca, modelo, valor  crie um segundo documento main com variável referência carro 1, carro 2, carro 3 , insira valores diferentes para cada variável através de um input recebendo o objeto, imprima no terminal o espaço  alocado de memória do objeto principal , e de cada variável de referência para o objeto!

class Carro:

    def __init__(self, marca, modelo, valor):
        
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        
        
    def __str__(self):
        return (f'{self.marca} - {self.modelo} - {self.valor}')