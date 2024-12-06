def digitosDiferentes(n):
    diferentes = []
    n_str = str(n)
    for digito in n_str:
        if digitos not in diferentes:
            diferentes.append(digito)

    return 1 if len(diferentes) == len(n_str) else 0

while True:
    try:
        minimo, maximo = [int(x) for x in input().split()]
        contador = 0

        for i in range(minimo, maximo + 1):
            contador += digitosDiferentes(i)

        print(contador)

    except EOFError:
        break