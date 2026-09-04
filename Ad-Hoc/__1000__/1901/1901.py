class Butterflies:
    @staticmethod
    def resolve():
        N = int(input())
        grid = [[int(x) for x in input().split()] for _ in range (N)]
        collected_butterflies = set()
        
        for _ in range(N * 2):
            x, y = [int(x) for x in input().split()]
            bf = grid[x-1][y-1]
            
            collected_butterflies.add(bf)
            
        print(len(collected_butterflies))
        
Butterflies.resolve()