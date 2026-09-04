class Grandma_Vitórias_Piggy_Banks:
    @staticmethod
    def solve(n: int) -> None:
        j, z = 0, 0 
        for _ in range(n):
            a, b = [int(x) for x in input().split()]
            j += a; z += b
            print(j - z)
     
i = 1       
while True:
    n = int(input())
    if n == 0: break 
    
    print(f"Teste {i}")
    Grandma_Vitórias_Piggy_Banks.solve(n)
    print()
    i += 1