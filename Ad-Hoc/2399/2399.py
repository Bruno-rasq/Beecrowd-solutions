class Campo_Minado:
    @staticmethod
    def resolve():
        N = int(input())
        
        line = [0] + [int(input()) for _ in range(N)] + [0]
        
        for i in range(1, N + 1):
            bombs = 0
            if line[i - 1] == 1: bombs += 1
            if line[i] == 1: bombs += 1
            if line[i + 1] == 1: bombs += 1
            
            print(bombs)
            
Campo_Minado.resolve()