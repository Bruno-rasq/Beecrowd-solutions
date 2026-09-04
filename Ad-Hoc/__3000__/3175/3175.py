ans = 0
n = int(input())
gooddeeds = [int(x) for x in input().split()]
uniques = set(gooddeeds)
levels = sorted(set(gooddeeds))
gift = {}

for i, value in enumerate(levels):
    gift[value] = i + 1

ans = 0
for x in gooddeeds:
    ans += gift[x]

print(ans)