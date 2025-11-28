from collections import deque

ROWS, COLS = map(int, input().split())
nut_str = input().strip()
MAZE_BOLT = [list(input().strip()) for _ in range(ROWS)]

# índices onde há relevos (1s)
nut = [i for i, ch in enumerate(nut_str) if ch == "1"]

def rotated_positions(offset):
    return [(i + offset) % COLS for i in nut]

def collides(offset, screw):
    return any(screw[i] == "1" for i in rotated_positions(offset))

def fits(offset, screw):
    return all(screw[i] == "0" for i in rotated_positions(offset))

# BFS
def solve():
    queue = deque()
    visited = set()

    # estado inicial: nível 0, offset livre (screw vazio)
    for off in range(COLS):
        queue.append((0, off))
        visited.add((0, off))
    
    while queue:
        lvl, off = queue.popleft()

        # terminou todos os níveis -> sucesso
        if lvl == ROWS:
            return True

        current_screw = ["0"] * COLS if lvl == 0 else MAZE_BOLT[lvl - 1]
        next_screw = MAZE_BOLT[lvl]

        # 1️⃣ tenta subir
        if fits(off, next_screw) and (lvl + 1, off) not in visited:
            queue.append((lvl + 1, off))
            visited.add((lvl + 1, off))

        # 2️⃣ tenta girar esquerda e direita
        for direction in (-1, 1):
            new_off = (off + direction) % COLS
            if not collides(new_off, current_screw) and (lvl, new_off) not in visited:
                queue.append((lvl, new_off))
                visited.add((lvl, new_off))
    
    return False

print("Y" if solve() else "N")