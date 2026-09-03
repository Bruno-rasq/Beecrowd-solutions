# número de ruas
n = int(input())

mapa = []
for _ in range(n + 1):
    mapa.append([int(x) for x in input().split()])

for i in range(n):
    line = ""
    for j in range(n):
        pa = mapa[i][j]
        pb = mapa[i][j + 1]
        pc = mapa[i + 1][j]
        pd = mapa[i + 1][j + 1]
        total = pa + pb + pc + pd
        line += "S" if total >= 2 else "U"
    print(line)