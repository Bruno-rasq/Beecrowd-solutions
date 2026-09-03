def busca_binaria_primeira_ocorrencia(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            resultado = meio       # guarda a posição
            fim = meio - 1         # continua buscando à esquerda
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


i = 1
while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break

    bolinhas_gude = [int(input()) for _ in range(n)]
    bolinhas_gude.sort()

    querys = [int(input()) for _ in range(q)]

    print(f"CASE# {i}:")

    for query in querys:
        idx = busca_binaria_primeira_ocorrencia(bolinhas_gude, query)
        if idx != -1:
            print(f"{query} found at {idx + 1}")
        else:
            print(f"{query} not found")

    i += 1