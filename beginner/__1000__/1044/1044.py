a, b = [int(x) for c in input().split()]

if a < b:
    temp = b
    b = a
    a = temp

print("Sao Multiplos" if a % b == 0 else "Nao sao Multiplos")