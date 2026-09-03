from collections import deque
import sys

input = sys.stdin.buffer.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

blemishes = 0
for i in range(N):
    row = grid[i]
    for j in range(M):
        if row[j]:
            blemishes += 1
            row[j] = 0
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if x > 0 and grid[x-1][y]:
                    grid[x-1][y] = 0
                    q.append((x-1, y))

                if x+1 < N and grid[x+1][y]:
                    grid[x+1][y] = 0
                    q.append((x+1, y))

                if y > 0 and grid[x][y-1]:
                    grid[x][y-1] = 0
                    q.append((x, y-1))

                if y+1 < M and grid[x][y+1]:
                    grid[x][y+1] = 0
                    q.append((x, y+1))

print(blemishes)