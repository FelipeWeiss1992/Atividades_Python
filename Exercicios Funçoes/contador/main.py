from controller import contador
from time import sleep

def main():
    contador(1, 10, 1)
    sleep(1)
    contador(10, 1, 2)
    sleep(1)
    print('-='*10,'Contagem Personalizada', '-='*10)
    contador(int(input('Digite o Inicio: ')),int(input('Digite o Fim: ')),int(input('Digite o Passo: ')))

main()    