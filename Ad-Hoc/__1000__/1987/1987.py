class Divisibility_by_3:
    @staticmethod
    def solve(n: str) -> None:
        sum_ = sum([int(x) for x in n])
        print(f"{sum_} sim" if sum_ % 3 == 0 else f"{sum_} nao")
        
while True:
    try:
        size, n = input().split()
        Divisibility_by_3.solve(n)
    except EOFError: break