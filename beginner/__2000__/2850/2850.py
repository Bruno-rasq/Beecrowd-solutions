while True:
    try:
        entrada = input()
        if entrada == "esquerda":
            print("ingles")
        if entrada == "direita":
            print("frances")
        if entrada == "nenhuma":
            print("portugues")
        if entrada == "as duas":
            print("caiu")

    except EOFError:
        break