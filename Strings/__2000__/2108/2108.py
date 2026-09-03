maior = 0
maior_palavra = ""

while True:
    try:
        ENTRADA = input()
        if ENTRADA == '0':
            break

        palavras = ENTRADA.split()
        response = []

        for palavra in palavras:
            if len(palavra) >= maior:
                maior = len(palavra)
                maior_palavra = palavra

            response.append(str(len(palavra)))

        print("-".join(response).strip())

    except EOFError:
        break

print('')
print(f"The biggest word: {maior_palavra}")