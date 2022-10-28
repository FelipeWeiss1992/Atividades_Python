def mediaNotas(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4
    

def aprovacao(media):
    if media >= 7:
      return 'Aprovado'
    
    elif media > 5:
      return 'Recuperação'
        
    else:
        return 'Reprovado'