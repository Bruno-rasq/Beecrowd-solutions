import math

n = int(input())
for _ in range(n):
    COORDENADAS = [int(x) for x in input().split()]
    ARESTAS = []
    
    i = 0
    for _ in range(3):
        ax, ay = COORDENADAS[i], COORDENADAS[(i + 1) % 6]
        bx, by = COORDENADAS[(i + 2) % 6], COORDENADAS[(i + 3) % 6]
        i += 2
    
        dist = math.sqrt((by - ay)**2 + (bx - ax)**2)
        ARESTAS.append(dist)
    
    
    p = (ARESTAS[0] + ARESTAS[1] + ARESTAS[2]) / 2
    area = math.sqrt(p * (p - ARESTAS[0]) * (p - ARESTAS[1]) * (p - ARESTAS[2]))
    
    print(f"{area:.3f}")