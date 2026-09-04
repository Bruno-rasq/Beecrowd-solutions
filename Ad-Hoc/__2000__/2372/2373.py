casos = int(input())

def tolist(s):
    return [int(elemento) for elementoin s.split()]


def copos_quebrados(bandejas):
    total = 0
    for bandeja in bandejas:
        latas, copos = tolist(bandeja)
        if latas > copos:
            total += copos
    print(total)


bandejas = []
for n in range(casos):
    curr = input()
    bandejas.append(curr)
    

copos_quebrados(bandejas)