def repeticoes_maximas(peso, rep):
    return peso * ( 1 + (rep / 30))

medias = []

while True:
    w1, w2, reps = [int(x) for x in input().split()]
    if w1 == w2 == resp == 0:
        break

    w1_max = repeticoes_maximas(w1, reps)
    w2_max = repeticoes_maximas(w2, reps)
    media_rm = (w1_max + w2_max) / 2
    medias.append(media_rm)

    if 1 <= media_rm < 13:
        print("Nao vai da nao")

    elif 13 <= media_rm < 14:
        print("E 13")

    elif 14 <= media_rm < 40:
        print("Bora, hora do show! BIIR!")

    elif 40 <= media_rm <= 60:
        print("Ta saindo da jaula o monstro!")

    elif media_rm > 60:
        print("AQUI E BODYBUILDER!!")

media_geral = sum(medias) /  len(medias) if medias else 0
if media_geral > 40:
    print()
    print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")