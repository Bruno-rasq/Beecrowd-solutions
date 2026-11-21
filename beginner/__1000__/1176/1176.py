fib = [0, 1]
while len(fib) < 61:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])

T = int(input())
for _ in range(T):
    N = int(input())
    print(f"Fib({N}) = {fib[N]}")