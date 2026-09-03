FIB = [1, 2]
for _ in range(41):
    x = FIB[-1]
    y = FIB[-2]
    FIB.append(x + y)
    
while True:
    n = int(input())
    if n == 0: break

    print(FIB[n - 1])