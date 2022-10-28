def mediaNotas(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        print('Aluno Aprovado')
         
    elif media > 5:
        print('Aluno em Recuperação')   
         
    else:
        print('Aluno Reprovado ')
        
        return media       