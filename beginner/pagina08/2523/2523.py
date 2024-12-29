while True:
    try:
        letras_alfabeto = input()
        quantidade_caracteres = int(input())
        caracteres = [int(n) for n in input().split()]

        mensagem = ""

        for i in range(quantidade_caracteres):
            mensagem += letras_alfabeto[caracteres[i] - 1]

        print(mensagem)
    except EOFError:
        break