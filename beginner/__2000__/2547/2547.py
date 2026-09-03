while True:
    try:

        participantes, altura_minima, altura_maxima = [
            int(x) for x in input().split()
        ]

        total_participantes_habeis = 0

        for _ in range(participantes):
            altura = int(input())
            if altura_minima <= altura <= altura_maxima:
                total_participantes_habeis += 1

        print(total_participantes_habeis)

    except EOFError:
        braak