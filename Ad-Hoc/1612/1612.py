class Little_Ant:
    @staticmethod
    def solve(n: int) -> None:
        out = n // 2 if n % 2 == 0 else (n // 2) + 1
        print(out)
        
N = int(input())
for _ in range(N):
    x = int(input())
    Little_Ant.solve(x)