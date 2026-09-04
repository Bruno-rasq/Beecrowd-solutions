data = [int(x) for x in input().split()]
N, M = data[0], data[1]  # tamanho do grid
X, Y = data[2], data[3]  # tamanho da seção
grid = [[int(x) for x in input().split()] for _ in range(N)]

max_lote_value = 0

while len(grid) > 0:
    # pega X linhas
    bloco = []
    for _ in range(X):
        bloco.append(grid.pop(0))

    # agora corta em blocos de colunas (Y por vez)
    while len(bloco[0]) > 0:
        lote = []
        for linha in bloco:
            lote.extend(linha[:Y])  # pega as Y primeiras colunas
            del linha[:Y]           # remove essas colunas da linha
        
        max_lote_value = max(max_lote_value, sum(lote))
        
print(max_lote_value)