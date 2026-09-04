from collections import deque

# 1 -> celula vazia e acessível
# 2 -> celula não acessível 
# 3 -> posição inicial do duende 
# 0 -> saida 

def find_adj_cells(matrix, x, y):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # apenas 4 direções
    adj_cells = []
    for dx, dy in delta:
        nx, ny = x + dx, y + dy 
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            if matrix[nx][ny] != 2:
                adj_cells.append((nx, ny))
    return adj_cells
    
def BFS(matrix, pi, targets):
    if pi in targets: return 0
    
    queue = deque([(pi, 0)])   # corrigido
    visiteds = set()
    visiteds.add(pi)
    
    while queue:
        curr, moves = queue.popleft()
        x, y = curr
        
        for next_pos in find_adj_cells(matrix, x, y):
            if next_pos in targets: 
                return moves + 1
            if next_pos not in visiteds:
                visiteds.add(next_pos)
                queue.append((next_pos, moves + 1))
    
    return -1  # caso não exista saída

class Duende_Perdido:
    @staticmethod
    def solve():
        rows, cols = [int(x) for x in input().split()]
        matrix, pos, exits = [], None, []
        
        for i in range(rows):
            line = [int(x) for x in input().split()]
            for j in range(cols):
                if line[j] == 3: pos = (i, j)
                if line[j] == 0: exits.append((i, j))
            matrix.append(line)
            
        out = BFS(matrix, pos, exits)
        print(out)

Duende_Perdido.solve()