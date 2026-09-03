import math

while True:
    v1, v2, AT, D = [int(x) for x in input().split()]
    if v1 == v2 == AT == D == 0: break

    P = AT / 6                  # CHANCE DO J1 VENCER O TURNO
    Q = 1 - P                   # CHANCE DO J2 VENCER O TURNO
    EV1 = math.ceil(v1 / D)     # HITS QUE J1 PRECISA LEVAR
    EV2 = math.ceil(v2 / D)     # HITS QUE J2 PRECISA LEVAR

    if P == Q:
        # Caso AT = 3: ambos têm 50% de chance
        PROBABILIDADE = EV1 / (EV1 + EV2)

    else:
        PROBABILIDADE = (1 - (Q/P)**EV1) / (1 - (Q/P)**(EV1 + EV2))

    print(f"{(PROBABILIDADE * 100.0):.1f}")