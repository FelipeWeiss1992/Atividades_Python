from controller import mediaNotas

def main():

    nome = str(input('Digite seu nome:'))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a primeira nota: '))
    n3 = float(input('Digite a primeira nota: '))
    n4 = float(input('Digite a primeira nota: '))
    media = mediaNotas(n1, n2, n3, n4)
    print(f'A média do aluno {nome} referente as notas: {n1} | {n2} | {n3} | {n4} é {media}')

main()
