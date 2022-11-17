def salvar(nome):
    with open('Cadastro_Pessoa\pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('Cadastro_Pessoa\pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.split()
            nomes.append(name) 
        return nomes





