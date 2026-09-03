n = int(input())

while n > 0:
    n -= 1
    l = int(input())
    vet = input().split()

    swaps = 0
    for i in range(l):
        for k in range(i + 1, l):
            if(int(vet[i]) > int(vet[k])):
                vet[i], vet[k] = vet[k], vet[i]
                swaps += 1

    print(f"Optimal train swapping takes {swaps} swaps.")

    #TLE