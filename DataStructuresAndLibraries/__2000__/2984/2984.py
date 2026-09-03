entrada = input()

pendentes = 0

for char in entrada:
    if char == "{":
        pendentes += 1
    elif char == "}" and pendentes > 0:
        pendentes -= 1

print('Partiu RU!' if pendentes == 0 else f"Ainda temos {pendentes} assunto(s) pendente(s)!")