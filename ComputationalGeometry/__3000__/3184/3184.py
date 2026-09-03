from collections import deque

WIDTH, HEIGHT = [int(x) for x in input().split()]
BOARD = []
PLAYER = [0, 0]

# LÊ OS DADOS DE INPUT DO BOARD E A POSIÇÃO DO PLAYER
for r in range(HEIGHT):
    ROW = input()

    for c in range(WIDTH):
        if ROW[c] == 'P':
            PLAYER = [r, c]

    BOARD.append(ROW)

GETTING_GOLD = set()
queue = deque()
visiteds = set()

x, y = PLAYER

visiteds.add(f"{x},{y}")
queue.append([x, y])

while len(queue) > 0:
    curr = queue.popleft()

    x, y = curr
    ux, uy = x - 1, y
    rx, ry = x, y + 1
    dx, dy = x + 1, y
    lx, ly = x, y - 1

    up = BOARD[ux][uy]
    right = BOARD[rx][ry]
    down = BOARD[dx][dy]
    left = BOARD[lx][ly]

    # Se estiver ao lado de uma armadilha,
    # não continua a exploração a partir dessa posição.
    if up == 'T' or right == 'T' or down == 'T' or left == 'T': continue

    # UP
    if up != '#':
        coord = f"{ux},{uy}"
        if up == 'G':
            GETTING_GOLD.add(coord)
        if up != 'T' and coord not in visiteds:
            visiteds.add(coord)
            queue.append([ux, uy])

    # RIGHT
    if right != '#':
        coord = f"{rx},{ry}"
        if right == 'G':
            GETTING_GOLD.add(coord)
        if right != 'T' and coord not in visiteds:
            visiteds.add(coord)
            queue.append([rx, ry])

    # DOWN
    if down != '#':
        coord = f"{dx},{dy}"
        if down == 'G':
            GETTING_GOLD.add(coord)
        if down != 'T' and coord not in visiteds:
            visiteds.add(coord)
            queue.append([dx, dy])

    # LEFT
    if left != '#':
        coord = f"{lx},{ly}"
        if left == 'G':
            GETTING_GOLD.add(coord)
        if left != 'T' and coord not in visiteds:
            visiteds.add(coord)
            queue.append([lx, ly])

print(len(GETTING_GOLD))