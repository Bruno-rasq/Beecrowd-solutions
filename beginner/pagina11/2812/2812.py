n = int(input())

for _ in range(n):
    tamanho_lista = int(input())
    lista = [int(x) for x in input().split()]
    
    impares = [n for n in lista if n % 2 != 0]
    lista_ordenada = []

    while impares:
        maior = max(impares)
        impares.remove(maior)
        lista_ordenada.append(maior)

        if impares:  # evita erro se a lista estiver vazia
            menor = min(impares)
            impares.remove(menor)
            lista_ordenada.append(menor)

    print(" ".join([str(n) for n in lista_ordenada]))