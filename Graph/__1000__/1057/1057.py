"""
Regras do movimento dos robôs:

1. Os 3 robôs (A, B, C) recebem o mesmo comando de direção simultaneamente.
2. Cada robô tenta mover para a célula adjacente na direção do comando.
   - Se for parede (#) ou fora do grid → ele fica parado.
3. Se um robô tenta mover para a célula ocupada por outro que ficou parado → ele também fica parado.
4. Se dois robôs tentarem trocar de lugar (swap) no mesmo movimento → movimento inválido.
5. Se dois ou mais robôs acabarem na mesma célula → movimento inválido.
6. Objetivo: os 3 robôs terminarem cada um em um portal (X) distinto.

Estratégia:
- BFS sobre estados (posição de cada robô)
- Estados normalizados como tuple ordenado para reduzir simetria
- Pré-cálculo de movimentos válidos para cada célula (move_table) para acelerar
"""

from collections import deque

# 4 direções de movimento
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def build_move_table(grid):
    """Pré-calcula para cada célula qual seria o destino em cada direção"""
    n = len(grid)
    cell_id = lambda x, y: x * n + y  # converte (x,y) -> inteiro único
    move_table = {}

    for x in range(n):
        for y in range(n):
            if grid[x][y] == "#": continue
            cur_id = cell_id(x, y)
            move_table[cur_id] = []
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                # se é válido, vai; se não, fica
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != "#":
                    move_table[cur_id].append(cell_id(nx, ny))
                else:
                    move_table[cur_id].append(cur_id)
    return move_table, cell_id

def apply_move(move_table, robots_state, dir_idx):
    """
    Move todos os robôs simultaneamente em uma direção, respeitando as regras:
    - não entra em célula de robô parado
    - não permite swap
    - não permite sobreposição final
    Retorna novo estado normalizado ou None se movimento inválido.
    """
    # 1️⃣ Primeiro, tenta mover todos (ou ficam no mesmo lugar)
    tentative = [move_table[pos][dir_idx] for pos in robots_state]

    # 2️⃣ Quem ficou parado?
    stuck = {robots_state[i] for i in range(3) if tentative[i] == robots_state[i]}

    # 3️⃣ Se alguém tenta entrar na célula de um robô parado → ele também fica parado
    for i in range(3):
        if tentative[i] in stuck and tentative[i] != robots_state[i]:
            tentative[i] = robots_state[i]  # cancela movimento

    # 4️⃣ Verifica colisão final (duas células iguais)
    if len(set(tentative)) < len(tentative):
        return None  # colisão

    # 5️⃣ Evita troca de lugares (swap)
    for i in range(3):
        for j in range(i + 1, 3):
            if robots_state[i] == tentative[j] and robots_state[j] == tentative[i]:
                return None

    # 6️⃣ Se tudo ok, retorna estado ordenado (normalizado)
    return tuple(sorted(tentative))

def bfs(grid, robots, portals):
    """
    BFS sobre os estados (posição de cada robô)
    - robots: lista [(x,y), (x,y), (x,y)]
    - portals: lista [(x,y), (x,y), (x,y)]
    """
    n = len(grid)
    move_table, cell_id = build_move_table(grid)

    # Converte posições para IDs inteiros
    robots = tuple(sorted(cell_id(x, y) for x, y in robots))
    portals_set = frozenset(cell_id(x, y) for x, y in portals)

    visited = {robots}
    queue = deque([(robots, 0)])  # (estado, movimentos)

    while queue:
        state, moves = queue.popleft()

        # ✅ Vitória: conjunto de robôs == conjunto de portais
        if set(state) == portals_set:
            return moves

        for dir_idx in range(4):
            new_state = apply_move(move_table, state, dir_idx)
            if new_state is None:
                continue
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + 1))

    return "trapped"

class Going_together:
    @staticmethod
    def resolve():
        t = int(input().strip())
        for case in range(1, t + 1):
            n = int(input().strip())
            grid = []
            robots = []
            portals = []

            for i in range(n):
                row = list(input().strip())
                for j, cell in enumerate(row):
                    if cell in ("A", "B", "C"):
                        robots.append((i, j))
                        row[j] = "."  # vira célula livre
                    elif cell == "X":
                        portals.append((i, j))
                grid.append(row)

            moves = bfs(grid, robots, portals)
            print(f"Case {case}: {moves}")

Going_together.resolve()