n = int(input())

for _ in range(n):
    reguas = [int(el) for el in input().split()][1:]
    total = reguas[0]

    for i in range(1, len(reguas)):
        total = (total - 1) + reguas[i]

    print(total)