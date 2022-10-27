from controller import quantPessoas, mediaIdade, mulheres, idadeAcimaMedia
lista_pessoas = []

def main():
    while True:
        pessoa = {}
        
        pessoa['Nome'] = str(input('Digite seu nome:'))
        pessoa['Sexo'] = str(input('Digite o sexo: [M/F]')).upper()
        while True:
            if pessoa['Sexo'] not in 'MF':
                print('Opção Inválida, digite somente M ou F.')
                pessoa['Sexo'] = str(input('Digite o sexo: [M/F] ')).upper()
            if  pessoa['Sexo'] in 'MF':
                break
        pessoa['Idade'] = int(input('Digite sua Idade: '))
        lista_pessoas.append(pessoa.copy())
        while True:
            resp = str(input('Deseja Continuar: [S/N] ')).upper()
            if resp not in 'SN':
                print('Opção Inválida, digite somente S ou N.')
            else:
                break
        if resp in 'N':
            break
        
main()
print()
print(f'Lista de Pessoas Cadastradas: {lista_pessoas}\n')
print(f'Ao todo foram cadastradas {quantPessoas(lista_pessoas)} pessoas.\n')
print(f'A média de todas as idades cadastradas é {mediaIdade(lista_pessoas):.2f}\n')
print(f'As mulheres cadastradas são {mulheres(lista_pessoas)}.\n')
print(f'As pessoas cadastradas acima da média são {idadeAcimaMedia(lista_pessoas)}\n')

