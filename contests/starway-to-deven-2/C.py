PI = 3.14

p, c, v = [int(n) for n in input().split()]

distancia_por_minuto = PI * p * v

tempo = c / distancia_por_minuto

print(f"{tempo:.2f}")