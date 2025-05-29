#na matrix original cada valor é representa por 1 ou 0,
# 0 se não houver pão de queijo (ai tenho que calcular a wnt adjacentes)
# 1 indica que há um pão de queijo (deve trocar todos os 1 por 9)

#direcoes no eixo x e y
DIRECOES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


while True:
    try:
        
        n_linhas, m_colunas = [int(x) for x in input().split()]
        matrix = [[int(x) for x in input().split()] for _ in range(n_linhas)]
        output = []
        
        for linha in range(n_linhas):
            linha_output = ""
            for coluna in range(m_colunas):
                
                curr = matrix[linha][coluna]
                
                if curr == 1:
                    linha_output += str(9)
                    continue
                
                adjacentes_nao_vazios = 0
                for dx, dy in DIRECOES:
                    ni, nj = linha + dx, coluna + dy
                    
                    if 0 <= ni < n_linhas and 0 <= nj < m_colunas: #define os limites
                        adjacentes_nao_vazios += matrix[ni][nj]
                        
                linha_output += str(adjacentes_nao_vazios)
            output.append(linha_output)
        
        print("\n".join(output))
        
    except EOFError: break