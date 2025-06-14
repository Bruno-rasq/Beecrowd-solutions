while True:
    n = int(input())
    if n == 0: break

    numeros = [int(x) for x in input().split()]
    ocorrencias = {}
    
    for i in range(n):
        if not numeros[i] in ocorrencias:
            ocorrencias[numeros[i]] = 0
        ocorrencias[numeros[i]] += 1
        
    for numero in ocorrencias:
        if ocorrencias[numero] % 2 != 0:
            print(numero)