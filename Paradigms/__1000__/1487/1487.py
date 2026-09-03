instancia = 1
while True:
    n_itens, capacidade = [int(x) for x in input().split()]
    if n_itens == capacidade == 0: break

    itens = []
    for _ in range(n_itens):
        duracao, valor = [int(x) for x in input().split()]
        itens.append((duracao, valor))

    # KNAPSACK ILIMITADO
    tabela = [0] * (capacidade + 1)
    for w in range(1, capacidade + 1):
        for duracao, valor in itens:
            if duracao <= w:
                tabela[w] = max(tabela[w], tabela[w - duracao] + valor)

    print(f"Instancia {instancia}")
    print(tabela[capacidade])
    print()
    instancia += 1