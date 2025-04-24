t = int(input())
while t != 0:
    for _ in range(t):
        n = int(input())
        if (n - 1) % 2 == 0:
            print(2 * n - 1)
        else:
            print(2 * n - 2)
    t = int(input())