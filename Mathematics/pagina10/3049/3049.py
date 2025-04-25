

B, T = [int(x) for x in input().split()]

area_total_nota = 160 * 60

area_esquerda_nota = (B + T) * 60 / 2 #trapezio
area_direita_nota = area_total_nota - area_esquerda_nota

if area_direita_nota == area_esquerda_nota:
    print(0)
else:
    print(1 if area_esquerda_nota > area_direita_nota else 2)