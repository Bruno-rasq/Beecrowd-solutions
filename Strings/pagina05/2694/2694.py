import re

casos_teste = int(input())

for _ in range(casos_teste):
    line = input()
    numeros = re.findall(r'\d+', line)
    
    output = sum([int(x) for x in numeros])
    print(output)