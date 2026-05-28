def GCD(a, b):
    if b == 0: return a
    return GCD(b, a % b)
    
x, y = [int(x) for x in input().split()]
print(GCD(x, y))