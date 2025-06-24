import math
class Searching_for_nessy:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            n, m  = [int(x) for x in input().split()]
            total_cells = math.ceil((n-2)/3) * math.ceil((m-2)/3)
            print(total_cells)
            
Searching_for_nessy().resolve()