height, width = map(int, input().split())

matrix = []
for _ in range(height):
    line = input().strip()
    if " " in line:
        matrix.append(line.split())
    else:
        matrix.append(list(line))

K = int(input())

ans = 0

# Horizontal →
for row in range(height):
    for col in range(width - K + 1):
        digits = "".join(matrix[row][col + i] for i in range(K))
        ans = max(ans, int(digits))

# Diagonal ↘
for row in range(height - K + 1):
    for col in range(width - K + 1):
        digits = "".join(matrix[row + i][col + i] for i in range(K))
        ans = max(ans, int(digits))

print(ans)