while True:
    try:
        jogadores = int(input())
        doisTercos = jogadores * (2 / 3)

        votos = [int(x) for x in input().split()]
        votosImpeachment = 0

        for i in range(jogadores):
            if votos[i] == 1:
                votosImpeachment += 1

        print("impeachment" if votosImpeachment >= doisTercos else "acusacao arquivada")

    except EOFError:
        break