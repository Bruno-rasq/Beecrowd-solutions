
#coordenadas a bola
x, y = [int(x) for x in input().split()]

print(
    "dentro"
    if (0 <= x <= 432 and 0 <= y <= 468) else "fora")