numero_titans, tamanho_muralha = [int(x) for x in input().split()]

for _ in range(numero_titans):
    data = input().split()
    altura_titan = int(data[-1])
    nome_titan = " ".join(data[:-1])

    if altura_titan > tamanho_muralha:
        print(nome_titan)