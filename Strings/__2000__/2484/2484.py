def textoDesenho(entrada):
    entrada = " ".join(entrada)
    aux = entrada
    for i in range(len(entrada)):
        print(aux)
        if len(entrada) > 1:
            entrada = entrada[:-2]
        aux = (" " * (i + 1)) + entrada

while True:
    try:
        entrada = input().strip()
        if not entrada:
            break
        textoDesenho(entrada)
        print('')
    except EOFError:
        break