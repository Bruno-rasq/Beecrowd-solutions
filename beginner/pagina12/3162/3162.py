import math

def calcDistancia(x1, y1, z1, x2, y2, z2):
    return math.sqrt(
        ((x2 - x1) ** 2) +
        ((y2 - y1) ** 2) +
        ((z2 - z1) ** 2)
    )


n = int(input())
naves = []

for i in range(n):
    x, y, z = list(map(int, input().split()))
    naves.append([x, y, z])

for i in range(n):
    menorDistancia = float("inf")
    nax, nay, naz = naves[i]

    for j in range(n):
        if i != j:
            npx, npy, npz = naves[j]
            distancia = calcDistancia(nax, nay, naz, npx, npy, npz)

            if distancia < menorDistancia:
                menorDistancia = distancia

    if menorDistancia > 50: 
        print("B") 
    elif 20 < menorDistancia <= 50: 
        print("M")
    else:
        print("A")