def simular(chao, teto):
    n = len(chao)
    trocas = 0
    nivel_atual = chao[0]

    for i in range(1, n):
        proximo = chao[i]

        if proximo == 0:
            # buraco no caminho, precisa trocar
            chao, teto = teto, chao
            nivel_atual = chao[i - 1]
            trocas += 1
        elif proximo > nivel_atual:
            # obstáculo, precisa trocar
            chao, teto = teto, chao
            nivel_atual = chao[i - 1]
            trocas += 1
        else:
            # pode continuar andando
            nivel_atual = proximo

    return trocas


while True:
    try:
        N = int(input())
        teto = list(map(int, input().split()))
        chao = list(map(int, input().split()))

        # tenta começar no chão e no teto (invertendo)
        resultado_chao = simular(chao[:], teto[:])
        resultado_teto = simular(teto[:], chao[:])

        menor = min(resultado_chao, resultado_teto) + 1
        maior = max(resultado_chao, resultado_teto) - 1

        print(min(menor, maior))
    except EOFError:
        break