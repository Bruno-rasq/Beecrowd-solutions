
#def quicksort(arr):
    #if len(arr) <= 1: return arr
    #pivo = arr[len(arr) // 2][1]
    #left, middle, right = [], [], []
    #for nome, nivel in arr:
        #if nivel < pivo: left.append([nome, nivel])
        #if nivel == pivo: middle.append([nome, nivel])
        #if nivel > pivo: right.append([nome, nivel])
    #return quicksort(left) + middle + quicksort(right)
    

qnt_jogadores, qnt_times = [int(x) for x in input().split()]

times = [[] for _ in range(qnt_times)]

auxiliar = []
for _ in range(qnt_jogadores):
    nome, nivel = input().split()
    auxiliar.append([nome, int(nivel)])

auxiliar = sorted(auxiliar, key=lambda x: x[1])


contador = qnt_jogadores - 1
while contador >= 0:
    for i in range(qnt_times):
        if contador < 0:
            break
        times[i].append(auxiliar[contador][0])
        contador -= 1


for i, time in enumerate(times, start=1):
    print(f"Time {i}")
    for nome in sorted(time):
        print(nome)
    print()