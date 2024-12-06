while True:
    try:
        bacteria = input()
        codigo_genetico = input()

        print("Resistente" if codigo_genetico in bacteria else "Nao resistente")
    except EOFError:
        break