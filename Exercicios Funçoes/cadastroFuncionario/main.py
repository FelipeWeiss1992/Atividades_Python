from controller import validarCT, impressao
from datetime import date

def main():
    pessoa = {}
    pessoa['Nome'] = str(input('Digite seu Nome: '))
    pessoa['Nasc'] = date.today().year - int(input('Ano Nascimento: '))
    pessoa['CarteiraTrabalho'] = int(input('Nº da Carteira de Trabalho: (digite 0 caso nao possuir.): '))
    validarCT(pessoa)
    impressao(pessoa)
   
main()