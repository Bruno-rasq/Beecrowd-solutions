while True:
    N = int(input())
    
    if N == 0:
        break

    # Cria a matriz com 2^(i+j)
    matriz = [[2**(i + j) for j in range(N)] for i in range(N)]

    # Descobre o maior valor da matriz para definir o espaçamento
    maior = matriz[-1][-1]
    largura = len(str(maior))

    for linha in matriz:
        print(" ".join(f"{num:>{largura}}" for num in linha))

    print()