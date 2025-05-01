def gerar_matriz_concentrica(N):
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            valor = 1 + min(i, j, N - 1 - i, N - 1 - j)
            linha.append(valor)
        matriz.append(linha)
    return matriz

while True:
    N = int(input())
    if N == 0:
        break

    matriz = gerar_matriz_concentrica(N)
    
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()