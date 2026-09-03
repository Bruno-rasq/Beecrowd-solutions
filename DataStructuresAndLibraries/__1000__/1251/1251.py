#a ideia é usar as hash tables para contabilizar as frequências 
#com a qual cada caracter aparece. 
#depois disto ordenar esses registros por ordem crescente de valor
# e exibir o resultado no formato "caracterascii frequência"
#deixar uma linha em branco depois de cada teste.

resultados = []

while True:
    try:
        freq = {}
        line = input()

        for char in line:
            idx = ord(char)
            freq[idx] = freq.get(idx, 0) + 1

        def ordenar_por_frequencia(par):
            return (par[1], -par[0])  # frequência crescente, ASCII decrescente em empate

        sorted_freq = sorted(freq.items(), key=ordenar_por_frequencia)

        resultado = "\n".join(f"{k} {v}" for k, v in sorted_freq)
        resultados.append(resultado)

    except EOFError:
        break

# imprimir tudo com linha em branco entre os casos
print("\n\n".join(resultados))