A, B, C = [float(x) for x in input().split()]

perimetro = (A + B + C)
area = ((A + B) * C ) / 2
condicao = A < (B + C) and B < ( A + C) and C < (A + B)

print(f"Perimetro = {perimetro:.1f}" if condicao else f"Area = {area:.1f}")