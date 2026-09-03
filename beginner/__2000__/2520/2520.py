
#distancia de manhattan (movimentação vertical ou horizontal)
# Distância de Manhattan entre 1 e 2 na matriz

while True:
    try:
        n, m = [int(x) for x in input().split()]
        
        X = None
        Y = None
        
        for i in range(n):
            linha = [int(x) for x in input().split()]
            for j in range(m):
                if linha[j] == 1:
                    X = (i, j)
                elif linha[j] == 2:
                    Y = (i, j)
        
        # Cálculo da distância de Manhattan
        dist = abs(X[0] - Y[0]) + abs(X[1] - Y[1])
        print(dist)
        
    except EOFError:
        break