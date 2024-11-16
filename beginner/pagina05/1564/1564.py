while True:
    try:
        reclamacoes = int(input())

        if reclamacoes != 0:
            print("vai ter duas!")
        else:
            print("vai ter copa!")
    except EOFError:
        break