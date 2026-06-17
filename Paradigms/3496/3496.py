n = int(input())
shirts = [int(x) for x in input().split()]
shirts = sorted(shirts)
cost = 0
for i in range(1, n, 2):
    cost += shirts[i]
print(cost)