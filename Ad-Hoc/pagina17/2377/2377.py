tam_estrada_km, distancia_pedagios = [int(x) for x in input().split()]
custo_por_km, custo_por_pedagio = [int(x) for x in input().split()]

custo_total_viagem = 0
pedagio = distancia_pedagios
for i in range(1, tam_estrada_km + 1):
    if i == pedagio:
        custo_total_viagem += custo_por_pedagio
        pedagio += distancia_pedagios
    custo_total_viagem += custo_por_km
    
    
print(custo_total_viagem)