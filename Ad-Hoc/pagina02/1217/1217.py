qnt_dias = int(input())

kg_totais = 0
gasto_total = 0

for i in range(1, qnt_dias + 1):
    valor = float(input())
    frutas = input().split()
    kg_por_fruta = len(frutas)
    
    kg_totais += kg_por_fruta
    gasto_total += valor
    
    print(f"day {i}: {kg_por_fruta} kg")
    
media_kg_frutas = kg_totais / qnt_dias
media_valor_gasto = gasto_total / qnt_dias

print(f"{media_kg_frutas:.2f} kg by day")
print(f"R$ {media_valor_gasto:.2f} by day")