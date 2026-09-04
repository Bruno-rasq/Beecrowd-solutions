pontuacoes = [int(x) for x in input().split()]

tam = len(pontuacoes)

for i in range(tam):
    for j in range(tam - i - 1):
        if pontuacoes[j] > pontuacoes[j + 1]:
            temp = pontuacoes[j]
            pontuacoes[j] = pontuacoes[j + 1]
            pontuacoes[j + 1] = temp

print(pontuacoes[1])