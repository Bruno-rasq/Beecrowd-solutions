teclado = [
    [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "´"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
]

mapeamento = {}
for linha in teclado:
    for i in range(1, len(linha)):
        mapeamento[linha[i]] = linha[i - 1]

cache = {}

while True:
    try:
        frase = input()
        frase_corrigida = ""

        for char in frase:
            if char == " ":
                frase_corrigida += " "
            else:
                if char not in cache:
                    cache[char] = mapeamento.get(char, "")
                frase_corrigida += cache[char]
        print(frase_corrigida)
    except EOFError:
        break