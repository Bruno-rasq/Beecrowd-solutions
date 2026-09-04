tempos = [float(x) for x in input().split()]
competidores = ["Otavio", "Bruno", "Ian"]

menor_tempo = min(tempos)

# Conta quantas vezes o menor tempo aparece
if tempos.count(menor_tempo) > 1:
    print("Empate")
else:
    print(competidores[tempos.index(menor_tempo)])