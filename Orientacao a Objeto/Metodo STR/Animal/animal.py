class Animal():

    especie = ''
    cor = ''
    raça = ''
        
    def __str__(self):
        return (f'{self.especie} - {self.cor} - {self.raça}')