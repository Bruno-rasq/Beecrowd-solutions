# DESENVOLVER A FUNÇÃO PREENCHER DO PAINT. RECEBE UMA MATRIX NxM QUADRO
# E UMA COORDENADA X,Y E UMA COR, DEVE COLORIR TODA A AREA DESEJADA E
# EXIBIR O RESULTADO.

while True:
    try:
        
        N, M = [int(x) for x in input().split()]
        frame = [[int(x) for x in input().split()] for _ in range(N)]
        X, Y, Color = [int(x) for x in input().split()]

        X -= 1
        Y -= 1

        initial_color = frame[X][Y]

        head = 0
        queue = [(X, Y)]

        frame[X][Y] = Color
    
        while head < len(queue):
            curr = queue[head]
            head = head + 1
    
            for delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dx = curr[0] + delta[0]
                dy = curr[1] + delta[1]
    
                if dx >= 0 and dx < N and dy >= 0 and dy < M:
                    if frame[dx][dy] == initial_color:
                        frame[dx][dy] = Color
                        queue.append((dx, dy))
    
        for line in frame:
            print(" ".join(map(str, line)))

    except:
        break