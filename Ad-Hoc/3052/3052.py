from collections import deque

def get_adjacent(grid, x, y):
    """
    Regras:
    - Se abaixo for '.', continua descendo.
    - Se abaixo for '#', espalha para os lados enquanto houver suporte.
    """
    n, m = len(grid), len(grid[0])
    adj = []

    # Desce enquanto tiver '.'
    if x + 1 < n and grid[x + 1][y] == ".":
        nx = x
        while nx + 1 < n and grid[nx + 1][y] == ".":
            nx += 1
            adj.append((nx, y))
        return adj  # desceu, não precisa espalhar

    # Se está apoiado em '#', espalha para os lados
    if x + 1 < n and grid[x + 1][y] == "#":
        # esquerda
        ny = y
        while ny - 1 >= 0 and grid[x][ny - 1] == ".":
            ny -= 1
            adj.append((x, ny))
            if x + 1 < n and grid[x + 1][ny] == ".":  # encontrou queda
                break
        # direita
        ny = y
        while ny + 1 < m and grid[x][ny + 1] == ".":
            ny += 1
            adj.append((x, ny))
            if x + 1 < n and grid[x + 1][ny] == ".":  # encontrou queda
                break

    return adj

def BFS(grid, x, y):
    n, m = len(grid), len(grid[0])
    queue = deque([(x, y)])

    while queue:
        cx, cy = queue.popleft()
        for nx, ny in get_adjacent(grid, cx, cy):
            if grid[nx][ny] == ".":  # marca com água
                grid[nx][ny] = "o"
                queue.append((nx, ny))
    return grid

class Chuva:
    @staticmethod
    def solve():
        n, m = map(int, input().split())
        grid = [list(input().strip()) for _ in range(n)]

        # fonte inicial
        sources = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == "o"]

        for x, y in sources:
            BFS(grid, x, y)

        for line in grid:
            print("".join(line))
            
Chuva.solve()