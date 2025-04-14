n = int(input())
pessoas = [int(x) for x in input().split()]

min_v = min(pessoas)
idx = pessoas.index(min_v)

print(idx + 1)