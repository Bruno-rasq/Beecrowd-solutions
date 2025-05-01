def garrafas_no_segundo_dia(n, k):
    trocadas = n // k
    novas_vazias = trocadas
    sobraram = n % k
    return novas_vazias + sobraram

# Entrada
T = int(input())
for _ in range(T):
    n, k = [int(x) for x in input().split()]
    print(garrafas_no_segundo_dia(n, k))