def printmatriz():
    for line in matriz:
        print("".join(line))
    print("@")

def move(atual, prox):
    if 0 <= prox[0] < N and 0 <= prox[1] < N:
        matriz[atual[0]][atual[1]] = "O"
        matriz[prox[0]][prox[1]] = "X"
        printmatriz()
        return prox
    else:
        return atual  # Evita sair da matriz


N = int(input())
while N != 0:
    
    START = N // 2
    FIM = (N - 1, N - 1)
    curr = (START, START)
    steps = 1
    
    matriz = [["O" for _ in range(N)] for _ in range(N)]
    matriz[START][START] = 'X'
    
    printmatriz()
    
    
    while True:
        # ➡ Direita
        for _ in range(steps):
            if curr == FIM: break
            curr = move(curr, (curr[0], curr[1] + 1))
        if curr == FIM: break
    
        # ⬆ Cima
        for _ in range(steps):
            if curr == FIM: break
            curr = move(curr, (curr[0] - 1, curr[1]))
        if curr == FIM: break
    
        steps += 1
    
        # ⬅ Esquerda
        for _ in range(steps):
            if curr == FIM: break
            curr = move(curr, (curr[0], curr[1] - 1))
        if curr == FIM: break
    
        # ⬇ Baixo
        for _ in range(steps):
            if curr == FIM: break
            curr = move(curr, (curr[0] + 1, curr[1]))
        if curr == FIM: break
    
        steps += 1
        
    N = int(input())