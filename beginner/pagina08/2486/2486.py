tabela_comidas_quantidade_vitamina_c = [
    {"suco de laranja", 120},
    {"morango fresco",  85},
    {"mamao",           85},
    {"goiaba vermelha", 70},
    {"manga",           56},
    {"laranja",         50},
    {"brocolis",        34}
]

quantidade_minima_vitamina_c = 110
quantidade_maxima_vitamina_c = 130

casos = int(input())
while casos != 0:
    
    quantidade_de_vitamaina_total = 0
    for i in range(casos):
        quantidade, comida = input().split(" ", 1)
        quantidade = int(quantidade)

        for c in tabela_comidas_quantidade_vitamina_c:
            if comida == c:
                quantidade_de_vitamaina_total += c[1] * quantidade

    if quantidade_minima_vitamina_c <= quantidade_de_vitamaina_total <= quantidade_maxima_vitamina_c:
        print(f"{quantidade_de_vitamaina_total} mg")

    elif quantidade_de_vitamaina_total < quantidade_minima_vitamina_c:
        quantidade_faltante = quantidade_minima_vitamina_c - quantidade_de_vitamaina_total
        print(f"Mais {quantidade_faltante} mg")

    elif quantidade_de_vitamaina_total > quantidade_maxima_vitamina_c:
        quantidade_excedente = quantidade_de_vitamaina_total - quantidade_maxima_vitamina_c
        print(f"Menos { quantidade_excedente} mg")

    casps = int(input())