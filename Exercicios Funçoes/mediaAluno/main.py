from controller import mediaNotas,aprovacao

def main():

    nome = str(input('Digite seu nome:'))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a primeira nota: '))
    n3 = float(input('Digite a primeira nota: '))
    n4 = float(input('Digite a primeira nota: '))
    print(f'A média do aluno {nome} referente as notas: {mediaNotas(n1, n2, n3, n4)} \nPrimeira Nota: {n1}\nSegunda Nota: {n2} \nTerceira Nota: {n3} \nQuarta Nota: {n4} \n{nome} está em {aprovacao(mediaNotas(n1, n2, n3, n4))}')

main()