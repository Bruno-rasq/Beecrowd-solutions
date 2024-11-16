while True:
    n = int(input().strip())

    if n == 0:
        break

    presentes = list(map(int, input().strip().split()))

    pares = []
    for i in range(n):
        par = presentes[i] + presentes[2 * n - i - 1]
        pares.append(par)

    par_caro = max(pares)
    par_barato = min(pares)

    print(f"{par_caro} {par_barato}")
