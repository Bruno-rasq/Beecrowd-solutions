import math

n, m = map(int, input().split())
d = list(map(int, input().split()))

falta = m - n
soma = sum(d)
i = 0

while falta > 0:
    if all(x == d[0] for x in d):  # todos iguais
        ganho = d[0]
        dias_que_faltam = math.ceil(falta / ganho)
        i += dias_que_faltam
        break
    else:
        novo = math.ceil(soma / 30)
        soma += novo - d[0]
        falta -= novo
        d = d[1:] + [novo]
        i += 1

print(i)