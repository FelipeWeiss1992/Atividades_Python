'''
-Crie uma pasta base para o projeto chamada banco 
- Dentro desta pasta banco crie três pastas com os nomes de model, view e controller. 
- Na pasta raiz banco, crie um documento com namespace start.py
Na pasta model crie um documento com namespace conta.py 
Dentro deste documento crie uma classe Conta, esta classe deve conter dois atributos privados: agência, numero_agencia, inseridos diretamente na classe e insira dados fixos nestes atributos
Crie anotações de @property e @setter para cada atributo privado da nossa classe.
- Chame o método __str__ e retorne os atributos acessando as anotações de @property e @setter de agencia, numero_agencia, coloque ( ; ) na divisão entre  os atributos.'''

class Conta:

    __agencia = 'Blumenau'
    __numero_agencia = '0101'

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
        return f'{self.agencia}; {self. numero_agencia}'