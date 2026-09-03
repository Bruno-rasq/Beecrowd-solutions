import math

n = int(input())

def crescimento_popucional(PA, PB, GA, GB):
    response = 1
    for anos in range(1, 101):
        if PA > PB:
            break
        PA += int(PA * GA)
        PB += int(PB * GB)
        response += 1

    return "Mais de 1 seculo" if PA <= PB else f"{response - 1} anos."

for _ in range(n):
    pa, pb, ga, gb = input().split()

    pa = int(pa)
    pb = int(pb)
    ga = float(ga) / 100
    gb = float(gb) / 100

    crescimento = crescimento_popucional(pa, pb, ga, gb)

    print(crescimento)