from collections import deque

class Contamination:
    @staticmethod
    def resolve():
        while True:
            ROWS, COLS = [int(x) for x in input().split()]
            if ROWS == COLS == 0: break
        
            contaminated_water = "T"
            contaminateds, MAP = [], []
            
            for i in range(ROWS):
                row = list(input().strip())
                for j, cell in enumerate(row):
                    if cell == contaminated_water:
                        contaminateds.append((i, j))
                MAP.append(row)  # << Adiciona a linha toda UMA VEZ, não dentro do loop j
            
            contaminated_cells = Contamination.bfs_contamination(contaminateds, MAP, ROWS, COLS)
            
            for cell in contaminated_cells:
                MAP[cell[0]][cell[1]] = contaminated_water
                
            for row in MAP: print("".join(row))
            print()
    
    @staticmethod
    def find_adj_cells(cell, cols, rows, MAP):
        # Deslocamentos: topo, baixo, esquerda, direita
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        adjacent_cells = []
        
        for dx, dy in offsets:
            nx = cell[0] + dx
            ny = cell[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols:
                if MAP[nx][ny] != "X":
                    adjacent_cells.append((nx, ny))
        
        return adjacent_cells

    @staticmethod
    def bfs_contamination(start_positions, MAP, rows, cols):
        
        contaminated = set(start_positions)  # Set com as posições já contaminadas (os T iniciais)
        queue = deque(start_positions)       # Fila para BFS
        
        while queue:
            current = queue.popleft()
            for nx, ny in Contamination.find_adj_cells(current, cols, rows, MAP):
                if MAP[nx][ny] == 'A' and (nx, ny) not in contaminated:
                    contaminated.add((nx, ny))
                    queue.append((nx, ny))
        
        return contaminated
        
Contamination.resolve()