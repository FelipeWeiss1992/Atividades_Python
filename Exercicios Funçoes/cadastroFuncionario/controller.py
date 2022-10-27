from datetime import date

def validarCT(pessoa):
    if pessoa['CarteiraTrabalho'] != 0:
        pessoa['PrimeiroAnoContratação'] = int(input('Digite seu primeiro ano de contratação: '))
        pessoa['Salario'] = float(input('Digite o Salário: R$'))
        pessoa['aposentadoria'] = pessoa['PrimeiroAnoContratação'] - (date.today().year - pessoa['Nasc']) + 35
        return pessoa
  
  

def impressao(pessoa):
    for chave, valor in pessoa.items():
        print(f'{chave}: {valor}')  
