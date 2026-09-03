criancas = {}

while True:
    try:
        crianca = input()
        criancas[crianca.lower()] = crianca
    except EOFError:
        break

# Ordena pelas chaves (em minúsculo)
criancas = dict(sorted(criancas.items()))

# Pega o último item (convertendo para lista de valores)
print(list(criancas.values())[-1])