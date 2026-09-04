# vitórias, empates, saldo de gols de dois times C e F
cv, ce, cs, fv, fe, fs = [int(x) for x in input().split()]

pontos_C = (cv * 3) + ce
pontos_F = (fv * 3) + fe

if pontos_C > pontos_F:
    print("C")
elif pontos_F > pontos_C:
    print("F")
else:  # pontos iguais
    if cs > fs:
        print("C")
    elif fs > cs:
        print("F")
    else:
        print("=")