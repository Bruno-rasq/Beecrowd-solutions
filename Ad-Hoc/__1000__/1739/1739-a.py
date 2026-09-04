fib = [1,1]
threefib = []

def fibonacci(k):
    while len(threefib) < k:
        a, b = fib[-1], fib[-2]
        c = a + b
        fib.append(c)
        
        if "3" in str(c) or c % 3 == 0:
            threefib.append(c)
            
while True:
    try:
        n = int(input())
        
        if len(threefib) < n: fibonacci(n)
        print(threefib[n - 1])
            
    except EOFError: break