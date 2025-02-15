a, b = [int(x) for x in input().split()]
resp = 0

if a > b:
    resp = (24 - a) + b
elif  a < b:
    resp = b - a
elif a == b:
     resp = (24 - a) + b

print(f"O JOGO DUROU {resp} HORA(S)")