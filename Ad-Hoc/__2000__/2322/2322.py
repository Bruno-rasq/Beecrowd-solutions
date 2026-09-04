total_pecas = int(input())
pecas = [int(x) for x in input().split()]

for i in range(1, total_pecas + 1):
    if i not in pecas:
        print(i)
        break