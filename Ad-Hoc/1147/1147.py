class Knight_scape:
    BOARD = {
        "8a": (0, 0), "8b": (0, 1), "8c": (0, 2), "8d": (0, 3), "8e": (0, 4), "8f": (0, 5), "8g": (0, 6), "8h": (0, 7),
        "7a": (1, 0), "7b": (1, 1), "7c": (1, 2), "7d": (1, 3), "7e": (1, 4), "7f": (1, 5), "7g": (1, 6), "7h": (1, 7),
        "6a": (2, 0), "6b": (2, 1), "6c": (2, 2), "6d": (2, 3), "6e": (2, 4), "6f": (2, 5), "6g": (2, 6), "6h": (2, 7),
        "5a": (3, 0), "5b": (3, 1), "5c": (3, 2), "5d": (3, 3), "5e": (3, 4), "5f": (3, 5), "5g": (3, 6), "5h": (3, 7),
        "4a": (4, 0), "4b": (4, 1), "4c": (4, 2), "4d": (4, 3), "4e": (4, 4), "4f": (4, 5), "4g": (4, 6), "4h": (4, 7),
        "3a": (5, 0), "3b": (5, 1), "3c": (5, 2), "3d": (5, 3), "3e": (5, 4), "3f": (5, 5), "3g": (5, 6), "3h": (5, 7),
        "2a": (6, 0), "2b": (6, 1), "2c": (6, 2), "2d": (6, 3), "2e": (6, 4), "2f": (6, 5), "2g": (6, 6), "2h": (6, 7),
        "1a": (7, 0), "1b": (7, 1), "1c": (7, 2), "1d": (7, 3), "1e": (7, 4), "1f": (7, 5), "1g": (7, 6), "1h": (7, 7),
    }
    
    delta_knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    delta_pawn = [(1, -1),(1, 1)]
    
    @staticmethod
    def adj_cells(pos, delta):
        adj = set()
        for px, py in pos:
            for x, y in delta:
                dx, dy = x + px, y + py
                if 0 <= dx < 8 and 0 <= dy < 8:
                    adj.add((dx, dy))
        return adj
    
    @staticmethod
    def resolve():
        case = 1
        while True:
            knight_pos = input()
            if knight_pos == "0": break 
            
            panws_pos = []
            for _ in range(8):
                panws_pos.append(Knight_scape.BOARD[input()])
    
            adj_cells_panws = Knight_scape.adj_cells(
                panws_pos, Knight_scape.delta_pawn)   
                
            adj_cells_knight = Knight_scape.adj_cells(
                [Knight_scape.BOARD[knight_pos]], Knight_scape.delta_knight
            )
            
            secure_moviments = [cell for cell in adj_cells_knight if cell not in adj_cells_panws]
            
            print("Caso de Teste #" + f"{case}: {len(secure_moviments)} movimento(s).")
            case += 1
            
Knight_scape.resolve()