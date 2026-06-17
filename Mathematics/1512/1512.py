import math

def mmc(a, b):
    if a == 0 or b == 0: return 0
    return (a * b) // math.gcd(a, b)
    
while True:
    N, A, B = [int(x) for x in input().split()]
    if N == A == B == 0: break
    
    ans = (N // A) + (N // B) - (N // mmc(A, B))
    print(ans)