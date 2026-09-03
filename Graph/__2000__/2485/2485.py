from collections import deque

class Bicho_da_Goiaba:
    # Movimentos para 8 direções
    adjacentes = [
        (-1, 0),  # cima
        (1, 0),   # baixo
        (0, -1),  # esquerda
        (0, 1),   # direita
        (-1, -1), # diagonal superior esquerda
        (-1, 1),  # diagonal superior direita
        (1, -1),  # diagonal inferior esquerda
        (1, 1)    # diagonal inferior direita
    ]
    
    @staticmethod
    def BFS(matriz, start):
        rows, cols = len(matriz), len(matriz[0])
        sx, sy = start
        
        # Se o ponto inicial não tem goiabeira, nem começa
        if matriz[sx][sy] == 0:
            return 0
        
        fila = deque([((sx, sy), 0)])
        visitado = [[False]*cols for _ in range(rows)]
        visitado[sx][sy] = True
        
        max_dias = 0
        
        while fila:
            (x, y), dias = fila.popleft()
            max_dias = max(max_dias, dias)
            
            for dx, dy in Bicho_da_Goiaba.adjacentes:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    # só espalha para outra goiabeira não visitada
                    if not visitado[nx][ny] and matriz[nx][ny] == 1:
                        visitado[nx][ny] = True
                        fila.append(((nx, ny), dias + 1))
        
        return max_dias
                
    @staticmethod
    def resolve():
        number_cases_test = int(input())
        for _ in range(number_cases_test):
            rows, cols = [int(x) for x in input().split()]
            matrix = [[int(x) for x in input().split()] for _ in range(rows)]
            x, y = [int(x) for x in input().split()]
            
            # Converte para índice 0-based
            x -= 1
            y -= 1
            
            out = Bicho_da_Goiaba.BFS(matrix, (x, y))
            print(out)

Bicho_da_Goiaba.resolve()