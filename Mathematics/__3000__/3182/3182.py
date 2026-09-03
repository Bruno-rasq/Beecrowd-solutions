participantes, orçamento, hoteis, semanas = [int(x) for x in input().split()]

minimo = float("INF")

for _ in range(hoteis):
    custo_por_pessoa = int(input())
    vagas_por_semana = [int(x) for x in input().split()]

    for vagas in vagas_por_semana:
        if vagas >= participantes:
            custo = custo_por_pessoa * participantes

            if custo <= orçamento:
                minimo = min(minimo, custo)

if minimo == float("INF"):
    print("stay home")
else:
    print(minimo)