def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero ** 0.5):
        if numero % i == 0:
            return False

    return True

def contagem(moedas, salto):
    index = len(moedas) - 1
    soma = 0
    while index >= 0:
        soma += moedas[index]
        index -= salto
    return soma

while True:
    try:
        n = int(input())
        moedas = []

        for _ in range(n):
            moeda = int(input())
            moedas.append(moeda)

        salto = int(input())

        resultado = contagem(moedas, salto)

        if eh_primo(resultado):
            print("You're a coastal aircraft. Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I'll hit you.")

    except EOFError:
        break