import math

n = int(input())
scores = [int(x) for x in input().split()]

# 1. ORDENAR E REORGANIZAR PARA MAXIMIZAR OS PRODUTOS
# Ordena: [10, 60, 70, 70, 80, 80]
scores_ordenados = sorted(scores)

# Divide em posições ímpares e pares para criar o zigue-zague ideal
lado_a = scores_ordenados[::2]       # [10, 70, 80]
lado_b = scores_ordenados[1::2]      # [60, 70, 80]

# Inverte o lado B para fechar o círculo perfeitamente
scores_maximos = lado_a + lado_b[::-1] # [10, 70, 80, 80, 70, 60]

# 2. CALCULAR A ÁREA COM O ÂNGULO CORRETO (360 / n)
angulo_graus = 360 / n
angulo_radianos = math.radians(angulo_graus)

def Area(a, b):
    return (a * b * math.sin(angulo_radianos)) / 2

area_total = 0
for i in range(n):
    a, b = scores_maximos[i], scores_maximos[(i + 1) % n]
    area_total += Area(a, b)

print(f"{area_total:.3f}")