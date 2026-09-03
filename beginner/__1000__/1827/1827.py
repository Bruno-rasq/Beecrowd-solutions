class Square_Array_IV:
    @staticmethod
    def solve(N: int) -> None:
        M = N // 3
        matrix = [[0] * N for _ in range(N)]
        
        # diagonais
        j = N - 1
        for i in range(N):
            matrix[i][i] = 2
            matrix[i][j] = 3
            j -= 1
        
        # quadrado central de 1s
        for i in range(M, N - M):
            for j in range(M, N - M):
                matrix[i][j] = 1
        
        # centro = 4
        matrix[N // 2][N // 2] = 4
        
        # print
        for line in matrix:
            print("".join(str(x) for x in line))
            
while True:
    try:
        n = int(input())
        Square_Array_IV.solve(n)
        print()
    except EOFError:
        break