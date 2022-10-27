from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end = ' ', flush=True)
            cont += passo
            sleep(0.3)
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ', flush=True)
            cont -= passo
            sleep(0.3)
        print('FIM!')  