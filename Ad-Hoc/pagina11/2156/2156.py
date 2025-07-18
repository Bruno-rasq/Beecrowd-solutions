class The_Adventures_of_Pak_man:
    directions = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }
    
    @staticmethod
    def amount_of_tablets(pos, board, commands):
        tablets = 0
        facing = "R"  # sempre começa virado para a direita
        curr_row, curr_col = pos
        
        for command in commands:
            if command != "W":
                # apenas muda direção
                facing = command
                continue
            
            # tenta andar na direção atual
            dr, dc = The_Adventures_of_Pak_man.directions[facing]
            nr, nc = curr_row + dr, curr_col + dc
            
            if board[nr][nc] != "#":  # se não é parede
                if board[nr][nc] == "*":
                    tablets += 1
                    board[nr][nc] = " "  # remove pastilha após comer
                curr_row, curr_col = nr, nc
        
        print(tablets)
    
    @staticmethod
    def resolve():
        while True:
            rows, cols, commands = map(int, input().split())
            if rows == cols == commands == 0:
                break
        
            board, pak_position = [], None
            for i in range(rows):
                line = list(input().rstrip())
                for j in range(cols):
                    if line[j] == "<":
                        pak_position = (i, j)
                        line[j] = " "  # posição inicial vira espaço
                board.append(line)
                
            ord_commands = input().strip()
        
            The_Adventures_of_Pak_man.amount_of_tablets(
                pak_position, board, ord_commands
            )
        
The_Adventures_of_Pak_man.resolve()