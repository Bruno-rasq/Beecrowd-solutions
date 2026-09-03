from collections import defaultdict

first = True
while True:
    N = int(input())
    if N == 0: break

    if not first: print()
    first = False

    bucket = defaultdict(lambda: defaultdict(list))
    for _ in range(N):
        name = input()
        color, size = input().split()
        bucket[color][size].append(name)

    for color in sorted(bucket):
        for size in sorted(bucket[color], reverse=True):
            for name in sorted(bucket[color][size]):
                print(f"{color} {size} {name}")