from collections import deque

# o cavalo em um tabuleiro fe xadrez possue uma movimentação
# bem especifica (movimento em L), isso indica que dada uma 
# posição do cavalo, ele terá 8 casas adjacentes que pode alcan-
# çar. 

# A ideia é usar uma busca em largura, verificando todas as po-
# ssibilidades por camada, sendo cada camada um movimento.

class Chess:
    BOARD = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
    ]
    
    COLS = {
        "a": 1, "b":2, "c":3, "d":4, 
        "e":5, "f":6, "g":7, "h": 8
    }
    
    @staticmethod
    def find_knight_possible_moves(pi: str) -> list[str]:
        Knight_adj_cells = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        possible_moves = []
        
        for dx, dy in Knight_adj_cells:
            nx = Chess.COLS[pi[0]] + dx
            ny = int(pi[1]) + dy
            
            if 1 <= nx <= 8 and 1 <= ny <= 8:
                # Ajuste para índices 0-based:
                possible_moves.append(
                    Chess.BOARD[8 - ny][nx - 1]
                )
        
        return possible_moves
        
class Knight_Moves: 
    @staticmethod
    def BFS(pi: str, target: str) -> int:
        if pi == target:
            return 0
        
        queue = deque([(pi, 0)])  # fila com (posição, movimentos)
        visited = set()
        visited.add(pi)
        
        while queue:
            current, moves = queue.popleft()
            
            for next_pos in Chess.find_knight_possible_moves(current):
                if next_pos == target:
                    return moves + 1  # caminho encontrado!
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
                    
        return -1  # em teoria, isso nunca acontece em um tabuleiro 8x8
        
        
    @staticmethod
    def resolve():
        while True:
            try:
                pi, pf = input().split()
                m = Knight_Moves.BFS(pi, pf)
            
                print(f"To get from {pi} to {pf} takes {m} knight moves.")
            except EOFError: break 
            
Knight_Moves.resolve()