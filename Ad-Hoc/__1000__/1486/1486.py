def sliding_window(queue, K): #-> O(N)
    count_toothpicks = 0
    toothpick = 0
    for n in queue:
        if n == 1: toothpick += 1
        else:
            if toothpick >= K:
                count_toothpicks += 1
            toothpick = 0
            
    if toothpick >= K: count_toothpicks += 1
            
    return count_toothpicks

class Biochemical_Digital_Circuit:
    @staticmethod
    def solve():
        while True:
            P, N, C = [int(x) for x in input().split()]
            if P == N == C == 0: break 
        
            cells = [[int(x) for x in input().split()] for _ in range(N)]
            transposta = [list(coluna) for coluna in zip(*cells)]

            count_toothpicks = 0
            for queue in transposta:
                count_toothpicks += sliding_window(queue, C)
                
            print(count_toothpicks)
            
Biochemical_Digital_Circuit.solve()