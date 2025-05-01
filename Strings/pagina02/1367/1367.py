while True:
    n = int(input())
    if n == 0:
        break

    penalidades = {}
    resolvidas = set()
    tempo_total = 0
    acertos = 0

    for _ in range(n):
        questao, tempo, resultado = input().split()
        tempo = int(tempo)

        if resultado == "correct":
            if questao not in resolvidas:
                penalidade = penalidades.get(questao, 0)
                tempo_total += tempo + (penalidade * 20)
                acertos += 1
                resolvidas.add(questao)
        else:  # incorrect
            if questao not in resolvidas:
                penalidades[questao] = penalidades.get(questao, 0) + 1

    print(acertos, tempo_total)