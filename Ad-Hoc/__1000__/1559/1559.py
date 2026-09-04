# A logica que verifica se um movimento é válido para as linhas
# também serve para as colunas

# lembrando que se houver um elemento de valor 2048 então o Game
# acabou e não há mais movimentos possiveis.

class Game_2048:
    @staticmethod
    def move_row(board_row, left=True):
        if left:
            for i in range(3):
                j = i + 1
                # movimento possível se:
                # - célula à esquerda está vazia mas à direita tem número
                if board_row[i] == 0 and board_row[j] != 0: return True
                
                # - células adjacentes são iguais
                if board_row[i] == board_row[j] and board_row[i] != 0:
                    return True
        else:
        
            for i in range(3, 0, -1):
                j = i - 1
                if board_row[i] == 0 and board_row[j] != 0: return True
                if board_row[i] == board_row[j] and board_row[i] != 0:
                    return True
    
        return False

    @staticmethod
    def all_possible_moves(BOARD):
        left, right, up, down = False, False, False, False
        
        for row, col in zip(BOARD, zip(*BOARD)):
            # linha → esquerda/direita
            if Game_2048.move_row(row): left = True
            if Game_2048.move_row(row, False): right = True
        
            # coluna → cima/baixo
            col = list(col)  # zip retorna tupla, convertemos pra lista
            if Game_2048.move_row(col): up = True
            if Game_2048.move_row(col, False): down = True
            
            for i in range(4):
                if row[i] == 2048: return "NONE"
                if col[i] == 2048: return "NONE"
            
        moves = []
        if down: moves.append("DOWN")
        if left: moves.append("LEFT")
        if right: moves.append("RIGHT")
        if up: moves.append("UP")
        
        if len(moves) == 0: return "NONE"
        return " ".join(moves)
    
    
n_test_cases = int(input())
for _ in range(n_test_cases):
    BOARD = [[int(x) for x in input().split()] for _ in range(4)]
    moves = Game_2048.all_possible_moves(BOARD)
    
    print(moves)