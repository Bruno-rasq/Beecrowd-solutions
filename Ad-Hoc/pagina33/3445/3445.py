dias, gc_casa, gc_trabalho = [int(x) for x in input().split()]

def leva_guarda_chuva(choveu, viagem):
    global gc_casa, gc_trabalho

    if viagem:  # ida
        if choveu == "Y" or gc_trabalho == 0:
            if gc_casa > 0:
                gc_casa -= 1
                gc_trabalho += 1
                return "Y"
            else:
                return "N"
        else:
            return "N"
    else:  # volta
        if choveu == "Y" or gc_casa == 0:
            if gc_trabalho > 0:
                gc_trabalho -= 1
                gc_casa += 1
                return "Y"
            else:
                return "N"
        else:
            return "N"

for _ in range(dias):
    choveu_ida, choveu_volta = input().split()
    output = []
    output.append(leva_guarda_chuva(choveu_ida, True))
    output.append(leva_guarda_chuva(choveu_volta, False))
    print(" ".join(output))