while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    desenho = [input() for _ in range(N)]
    A, B = map(int, input().split())

    escA = A // N
    escB = B // M

    for linha in desenho:
        nova_linha = ''.join(c * escB for c in linha)
        for _ in range(escA):
            print(nova_linha)
    print()  # linha em branco após cada caso