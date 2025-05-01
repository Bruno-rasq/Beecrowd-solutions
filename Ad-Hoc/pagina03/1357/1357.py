class Braille:
    dicionario = {
        "0": [".*", "**", ".."],
        "1": ["*.", "..", ".."],
        "2": ["*.", "*.", ".."],
        "3": ["**", "..", ".."],
        "4": ["**", ".*", ".."],
        "5": ["*.", ".*", ".."],
        "6": ["**", "*.", ".."],
        "7": ["**", "**", ".."],
        "8": ["*.", "**", ".."],
        "9": [".*", "*.", ".."]
    }

    @staticmethod
    def braille_decimal():
        matrix = []
        resultado = []
        
        for i in range(3):
            linha = input().strip().split()
            if i == 0:
                matrix = [[bloco] for bloco in linha]
            else:
                for j, bloco in enumerate(linha):
                    matrix[j].append(bloco)
        
        for item in matrix:
            for chave, valor in Braille.dicionario.items():
                if item == valor:
                    resultado.append(chave)
                    break
        
        print("".join(resultado))

    @staticmethod
    def decimal_braille():
        nums = input().strip()
        for i in range(3):
            linha = []
            for n in nums:
                linha.append(Braille.dicionario[n][i])
            print(" ".join(linha))
            

while True:
    n = int(input())
    if n == 0:
        break

    operacao = input().strip()
    Braille.decimal_braille() if operacao == "S" else Braille.braille_decimal()