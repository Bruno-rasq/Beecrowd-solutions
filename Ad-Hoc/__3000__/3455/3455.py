grafica, dinamica, geometria = [int(x) for x in input().split()]
tipo_questao_desejada = input().strip()

total = 0

if tipo_questao_desejada == "A":  # Gráfica
    total += grafica
    total += dinamica * (3 / 2)  # 1 dinâmica = 1.5 gráficas
    total += geometria * 2.5     # 1 geometria = 2.5 gráficas
elif tipo_questao_desejada == "B":  # Dinâmica
    total += dinamica
    total += grafica * (2 / 3)   # 1 gráfica = 0.666 dinâmica
    total += geometria * 2.5 * (2 / 3)  # geometria -> gráfica -> dinâmica
elif tipo_questao_desejada == "C":  # Geometria
    total += geometria
    total += grafica * (1 / 2.5)       # 1 gráfica = 0.4 geometria
    total += dinamica * (3 / 2) * (1 / 2.5)  # dinâmica -> gráfica -> geometria

print(int(total))