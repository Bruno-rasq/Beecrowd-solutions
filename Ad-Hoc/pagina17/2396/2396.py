n. m = map(int, input().split())

resultados = []
for i in range(n):
    tempos = list(map(int, input().split()))
    soma = sum(tempos)
    resultados.append([i + 1, soma])

resultados.sort(key=lambda x: x[1])

for i in range(3):
    print(resultados[i][0])