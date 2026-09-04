
porcentagem1, porcentagem2 = [int(x) for x in input().split()]

if 0 <= porcentagem2 <= 2:
    print("nova")
elif 97 <= porcentagem2 <= 100:
    print("cheia")
elif porcentagem1 < porcentagem2:
    print("crescente")
else:
    print("minguante")