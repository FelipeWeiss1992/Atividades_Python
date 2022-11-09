# crie um documento instanciando uma classe chamada carro com atributos marca, modelo, valor. Crie  um método str  com a variável referência que acessa os atributos da classe no espaço alocado de memória.  insira os atributos na função através da variável referência padrão, e use f string para adicionar ao return. crie um segundo documento main com variável referência carro 1, carro 2, carro 3 , insira valores diferentes para cada objeto, imprima no terminal os dados inseridos

class Carro():

    marca = ''
    modelo = ''
    valor = 0
        
    def __str__(self):
        return (f'{self.marca} - {self.modelo} - {self.valor}')
