def numeros_sem_par(lista):
    freq = {}
    for num in lista:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    impares = [num for num in freq if freq[num] % 2 == 1]
    impares.sort()
    return " ".join(map(str, impares))

while True:
    try:
        n = input()
        lista = [int(x) for x in input().split()]
        print(numeros_sem_par(lista))
    except EOFError:
        break