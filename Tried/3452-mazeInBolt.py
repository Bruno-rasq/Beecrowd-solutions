from typing import List

ROWS, COLS = [int(x) for x in input().split()]
nut = [idx for idx, data in enumerate(input()) if data == "1"]
MAZE_BOLT = [[x for x in input()] for _ in range(ROWS)]

current_screw = ["0"] * COLS

# faz 1 rotacao para esquerda ou direita, caso contrario []
def rotate_nut(nut, screw, direction = 1) -> List:
    delta = [(idx + direction) % COLS for idx in nut]
    if all(screw[i] == "0" for i in delta): return delta
    return []

# checa se a posição da porca encaixa no parafuso
def check_fits(nut, next_screw) -> bool:
    return all(next_screw[idx] == "0" for idx in nut)

# tenta fazer rotações até encaixar ou não
def try_rotate(spin, curr_screw, next_screw, direction) -> List:
    while True:
        spin = rotate_nut(spin, curr_screw, direction)
        if spin == []: return []
        if check_fits(spin, next_screw): return spin

# tenta encaixar a porca no proximo nivel do parafuso
def try_fit(nut, curr_screw, next_screw) -> List:
    if check_fits(nut, next_screw): return nut
    
    spin_left = try_rotate(nut[:], curr_screw, next_screw, -1)  
    if spin_left != []: return spin_left  
      
    spin_right = try_rotate(nut[:], curr_screw, next_screw, 1)  
    if spin_right != []: return spin_right  
      
    return []

# valida se a porca resolve o labirinto do parafuso
def validate_nut_and_mazebolt(MAZE, nut, current_screw) -> bool:
    idx = 0
    while idx < ROWS:
        nut = try_fit(nut, current_screw, MAZE[idx])
        if nut == []: return False
        current_screw = MAZE[idx]
        idx += 1
    return True

out = validate_nut_and_mazebolt(MAZE_BOLT, nut, current_screw)
print("Y" if out else "N")