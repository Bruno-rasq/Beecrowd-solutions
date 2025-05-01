def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pode_chegar(total, atual, destino, sobe, desce):
    if sobe == 0 and desce == 0:
        return atual == destino  # Só possível se já estiver no destino
    if sobe == 0:
        return destino < atual and (atual - destino) % desce == 0
    if desce == 0:
        return destino > atual and (destino - atual) % sobe == 0

    diferenca = destino - atual
    return diferenca % mdc(sobe, desce) == 0

def menor_cliques(total, atual, destino, sobe, desce):
    visitados = [False] * (total + 1)
    fila = [(atual, 0)]  # tupla: (andar atual, número de cliques)
    visitados[atual] = True

    while fila:
        andar, cliques = fila.pop(0)

        if andar == destino:
            return cliques

        # Tenta subir
        proximo = andar + sobe
        if sobe > 0 and proximo <= total and not visitados[proximo]:
            visitados[proximo] = True
            fila.append((proximo, cliques + 1))

        # Tenta descer
        proximo = andar - desce
        if desce > 0 and proximo >= 1 and not visitados[proximo]:
            visitados[proximo] = True
            fila.append((proximo, cliques + 1))

    return -1  # impossível (caso não passe na verificação inicial)

# Entrada de dados
total, atual, destino, subir, descer = [int(x) for x in input().split()]

if pode_chegar(total, atual, destino, subir, descer):
    cliques = menor_cliques(total, atual, destino, subir, descer)
    print(f"{cliques}")
else:
    print("use the stairs")