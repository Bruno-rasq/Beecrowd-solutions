
import math

casos_teste = int(input())
for _ in range(casos_teste):
    
    pessoas, mililitros = map(int, input().split())
    b, B, H = map(int, input().split())
    
    media = mililitros / pessoas
    temp = (media * 3 * (B - b) / (math.pi * H) + b ** 3) ** (1/3)
    h = media * 3 / (math.pi * (temp ** 2 + temp * b + b ** 2))
    
    print(f"{h:.2f}")