import sys

while True:
    try:
        n = int(input())
        numeros = [input().strip() for _ in range(n)]

        # Ordenamos os números em ordem lexicográfica
        numeros.sort()

        digitos_economizados = 0

        for i in range(1, n):
            for j in range(len(numeros[i])):
                if numeros[i][j] != numeros[i-1][j]:  # Paramos ao encontrar um caractere diferente
                    break
                digitos_economizados += 1  # Contamos os caracteres economizados

        print(digitos_economizados)

    except EOFError:
        break