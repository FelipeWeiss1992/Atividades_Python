def mediaIdade(lista_pessoas):
    somaidade = 0
    for pessoas in lista_pessoas:
        if pessoas and 'Idade' in pessoas.keys():
            somaidade += pessoas['Idade']
    media_idade = somaidade / len(lista_pessoas)        
    return media_idade
    
def mulheres(lista_pessoas):
    mulheres = []
    for pessoas in lista_pessoas:
        if pessoas['Sexo'] in 'F':
            mulheres.append(pessoas)
    return mulheres
    
def idadeAcimaMedia(lista_pessoas):
    acimamedia = []
    somaidade = 0
    for pessoas in lista_pessoas:
        if pessoas and 'Idade' in pessoas.keys():
            somaidade += pessoas['Idade']
    media_idade = somaidade / len(lista_pessoas)
    for pessoas in lista_pessoas:
        if pessoas and 'Idade' in pessoas.keys():
            if pessoas['Idade'] > media_idade:
                acimamedia.append(pessoas)
    return acimamedia
   
