def jogadaValinda(pi, pf):

    deslocamentos = [
        (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    colunas = [
        "a": 1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h": 8
    ]

    colunas_inical = colunas[pi[0]]
    linha_inical = int(pi[1])

    for dx, dy in deslocamentos:
        nova_coluna = colunas_inical + dx
        nova_linha = linha_inical + dy

        if  nova_coluna == colunas[pf[0]] and nova_linha == int(pf[1]):
            return True

    return False

posicao_inical, pocisao_desejada = input().split()
print("VALIDO" if jogadaValinda(posicao_inical, pocisao_desejada) else "INVALIDA")