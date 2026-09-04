COORDENADA_BURACOS = {(1, 3), (2, 3), (2, 5), (5, 4)}

MOVES = {
    1: (1, 2),
    2: (2, 1),
    3: (2, -1),
    4: (1, -2),
    5: (-1, -2),
    6: (-2, -1),
    7: (-2, 1),
    8: (-1, 2)
}

n = int(input())
movimentos = list(map(int, input().split()))

pos = (4, 3)
count = 0

for m in movimentos:
    dx, dy = MOVES[m]
    x, y = pos[0] + dx, pos[1] + dy
    pos = (x, y)
    count += 1
    
    if pos in COORDENADA_BURACOS: break
    if not (0 <= x <= 7 and 0 <= y <= 7): break

print(count)