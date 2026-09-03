keys, frases = map(int, input().split())

digits = {}

for _ in range(keys):
    a, b = input().split()
    digits[a.lower()] = b.lower()
    digits[b.lower()] = a.lower()

for _ in range(frases):
    frase = input()
    frase_corrigida = []

    for char in frase:
        lower_char = char.lower()
        if lower_char in digits:
            mapped = digits[lower_char]
            if char.isupper():
                frase_corrigida.append(mapped.upper())
            else:
                frase_corrigida.append(mapped)
        else:
            frase_corrigida.append(char)

    print("".join(frase_corrigida))