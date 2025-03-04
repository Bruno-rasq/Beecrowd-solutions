from collections import defaultdict

n_test_cases = int(input())

class SudokuBoard:
    def isValidAswer(self, board: list[list[int]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                curr = board[row][column]
                
                if curr in rows[row] or curr in cols[column] or curr in boxes[(row//3, column//3)]:
                    return False
                    
                rows[row].add(curr)
                cols[column].add(curr)
                boxes[(row//3, column//3)].add(curr)
                
        return True
                

for i in range(n_test_cases):
    sudoku = []
    for _ in range(9):
        line = [int(x) for x in input().split()]
        sudoku.append(line)
        
    print(f"Instancia {i + 1}")
    board = SudokuBoard()
    print("SIM" if board.isValidAswer(sudoku) else "NAO")
    print("")