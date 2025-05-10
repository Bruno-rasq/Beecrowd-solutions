def max_lucro(valores_per_dia, custo):
    valores_atualizados = [val - custo for val in valores_per_dia]
    max_atual = max_total = 0

    for lucro in valores_atualizados:
        max_atual = max(lucro, max_atual + lucro)
        max_total = max(max_total, max_atual)

    return max_total


while True:
    try:
        dias = int(input())
        custo = int(input())
        valores_por_dia = []
        for _ in range(dias):
            valores_por_dia.append(int(input()))

        resutlado = max_lucro(valores_por_dia, custo)
        print(resutlado)

    except EOFError:
        break