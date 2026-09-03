n = int(input())

names = [input().strip() for _ in range(n)]
sorted_names = sorted(names, key= lambda name: name[0])

for name in sorted_names:
    print(name)