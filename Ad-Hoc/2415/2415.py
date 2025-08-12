class Consecutivos:
    @staticmethod
    def solve(values: list[int], n: int) -> None:
        curr, count, max_sequence = None, 1, 0
        
        for x in range(n):
            if curr == values[x]: count += 1
            else:
                if count > max_sequence: 
                    max_sequence = count
                count = 1
                curr = values[x]
                
        if count > max_sequence: max_sequence = count
                
        print(max_sequence)
        
N, values = int(input()), [int(x) for x in input().split()]
Consecutivos.solve(values, N)