while True:
    
    n_assinaturas_originais = int(input())
    if n_assinaturas_originais == 0: break

    assinaturas_originais, qnt_assinaturas_falsas = {}, 0
    
    for _ in range(n_assinaturas_originais):
        nome, assinatura_original = input().split()
        assinaturas_originais[nome] = assinatura_original
        
    n_assinaturas_do_dia = int(input())
    
    for _ in range(n_assinaturas_do_dia):
        nome, assinatura = input().split()
        assinatura_original = assinaturas_originais[nome]
        
        diferencas = 0
        for ind, char in enumerate(assinatura_original):
            if char != assinatura[ind]: diferencas += 1
            
        qnt_assinaturas_falsas += 1 if diferencas > 1 else 0
        
    print(qnt_assinaturas_falsas)