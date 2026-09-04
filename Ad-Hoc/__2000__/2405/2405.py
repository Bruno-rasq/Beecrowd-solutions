from collections import deque

def find_adj_cells(board, x, y):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (1, -1), (-1, 1), (1, 1)]
             
    adj_cells = []
    for dx, dy in delta:
        nx, ny = dx + x, dy + y
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] != 1: adj_cells.append((nx, ny))
            
    return adj_cells
    
def flood_fill(board, x, y):
    visiteds = set()
    visiteds.add((x, y))
    queue = deque([(x, y)])
    
    while queue:
        curr_x, curr_y = queue.popleft()
        for adj_cell in find_adj_cells(board, curr_x, curr_y):
            if adj_cell not in visiteds:
                queue.append(adj_cell)
                visiteds.add(adj_cell)
                
    return len(visiteds)
    
class Colorindo:
    @staticmethod
    def solve():
        N, M, X, Y, K = [int(i) for i in input().split()]
        board = [[0] * M for _ in range(N)]
        
        for _ in range(K):
            coord_x, coord_y = [int(x) for x in input().split()]
            board[coord_x - 1][coord_y - 1] = 1
        
        colored_cells = flood_fill(board, X - 1, Y - 1)
        print(colored_cells)
        
Colorindo.solve()