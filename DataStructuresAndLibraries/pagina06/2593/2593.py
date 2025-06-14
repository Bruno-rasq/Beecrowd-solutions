texto_completo = input().split()
qnt_palavras = int(input())
palavras_a_buscar = input().split()
ocorrencia_por_palavra = {palavra: [] for palavra in palavras_a_buscar}

indice = 0
for palavra in texto_completo:
    if palavra in ocorrencia_por_palavra:
        ocorrencia_por_palavra[palavra].append(str(indice))
    indice += len(palavra) + 1  # conta o espaço

for palavra in palavras_a_buscar:
    indices = ocorrencia_por_palavra[palavra]
    print(" ".join(indices) if indices else "-1")