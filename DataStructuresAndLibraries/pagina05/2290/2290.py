
from collections import Counter

def numeros_sem_par(lista):
    freq = Counter(lista)
    impares = [num for num, cont in freq.items() if cont & 1]
    impares.sort()
    return " ".join(map(str, impares))
    
while True:
    try:
        n = input()
        lista = [int(x) for x in input().split()]
        print(numeros_sem_par(lista))
    except EOFError: break