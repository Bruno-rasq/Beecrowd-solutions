import math

voltas, placas = map(int, input().split())

total_placas = voltas * placas

resultados = []

for porcentagem in range(10, 100, 10):
    quantidade_placas_por_porcentagem = math.ceil((total_placas * porcentagem) / 100)
    resultados.append(quantidade_placas_por_porcentagem)

print(" ".join(map(str, resultados)))