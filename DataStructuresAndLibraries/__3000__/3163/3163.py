# A logica da questão envolve a implementação simples de uma 
# fila prioritária, no protocolo do aeroporto as aeronas tem 
# as seguintes prioridade -1(Oeste), -3(Norte), -2(Sul), -4(Leste)
# para resolver basta intercalar as aeronaves seguindo esta ordem
# do protocolo

fila_oeste, fila_norte, fila_sul, fila_leste = [], [], [], []
fila_atual = None

while True:
    entrada = input().strip()
    if entrada == "0": break

    elif entrada in ["-1", "-2", "-3", "-4"]:
        fila_atual = entrada
    else:
        if fila_atual == "-1": fila_oeste.append(entrada)
        elif fila_atual == "-3": fila_norte.append(entrada)
        elif fila_atual == "-2": fila_sul.append(entrada)
        elif fila_atual == "-4": fila_leste.append(entrada)

# Lista com as filas na ordem do protocolo
filas = [fila_oeste, fila_norte, fila_sul, fila_leste]

resultado = []

# Enquanto houver pelo menos uma fila com aviões
while any(filas):
    for fila in filas:
        if fila:
            resultado.append(fila[0])
            del fila[0]

print(" ".join(resultado))

