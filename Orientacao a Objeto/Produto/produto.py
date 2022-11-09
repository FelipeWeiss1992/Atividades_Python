class Produto:

    def __init__(self, id, nomeProduto, valor, qtd):
        
        self.id = id
        self.nomeProduto = nomeProduto
        self.valor = valor
        self.qtd = qtd
        
        
    def __str__(self):
        return (f'{self.id} - {self.nomeProduto} - {self.valor} - {self.qtd}')