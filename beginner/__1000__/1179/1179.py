pares = []
impares = []

for _ in range(15):

    curr = int(input())
    
    if curr % 2 == 0:
        pares.append(curr)
        if pares.length == 5:
            for j in range(len(pares)):
                print(f"par[{j}] = {pares[j]}")
            pares = []
       
    else:
        impares.append(curr)
        if impares.length == 5:
            for j in range(len(impares)):
                print(f"impar[${j}] = ${impares[j]}")
            impares = []

for j, n in enumerate(impares):
    print(f"impar[{j}] = {n}")

for j, n in enumerate(pares):
    print(f"par[{j}] = {n}")