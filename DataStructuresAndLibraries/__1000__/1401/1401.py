def permutar(texto):
    # tamanho do set evita permutar palavras com chars iguais "aaa"
    if len(texto) == 1 or len(set(texto)) == 1: return [texto]
    
    permutacoes = set()
    
    for indice, caractere_fixo in enumerate(texto):
        restante = texto[:indice] + texto[indice+1:]
        permutacoes_restantes = permutar(restante)

        for permutacao in permutacoes_restantes:
            permutacoes.add(caractere_fixo + permutacao)

    return list(permutacoes)
    

numero_casos_teste = int(input())
for _ in range(numero_casos_teste):
    texto = input()
    permutacoes = sorted(permutar(texto))
    print("\n".join(permutacoes))
    print("")