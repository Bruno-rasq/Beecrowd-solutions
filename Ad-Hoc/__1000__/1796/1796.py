n = int(input())
opinioes = [int(o) for o in input().split()]

negativos = 0
positivos = 0

for i in range(n):
    if opinioes[i] == 0:
        positivos += 1
    else:
        negativos += 1

print("Y" if positivos > negativos else "N")