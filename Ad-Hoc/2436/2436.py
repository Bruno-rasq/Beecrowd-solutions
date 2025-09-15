def move(BOARD, pos_x, pos_y):
    ADJ_CELLS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in ADJ_CELLS:
        nx, ny = pos_x + dx, pos_y + dy 
        
        if 0 <= nx < len(BOARD) and 0 <= ny < len(BOARD[0]):
            if BOARD[nx][ny] == 1: return (nx, ny)
            
    return -1


class Robo:
    @staticmethod
    def solve():
        L, C = [int(x) for x in input().split()]
        X, Y = [int(x) for x in input().split()]
        
        BOARD = [[int(x) for x in input().split()] for _ in range(L)]
        curr_x, curr_y = X - 1, Y - 1
        
        while True:
            out = move(BOARD, curr_x, curr_y)
            
            if out == -1: break
        
            nx, ny = out
            BOARD[curr_x][curr_y] = 0
            curr_x, curr_y = nx, ny
            
        print(f"{curr_x + 1} {curr_y + 1}")
        
Robo.solve()