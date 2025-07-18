from collections import deque

class Colouring_Game_Scenarios:
    def __init__(self):
        self.r, self.c = [int(x) for x in input().split()]
        self.scenario = [list(input().strip()) for _ in range(self.r)]
        self.colored_areas = 0

        for i in range(self.r):
            for j in range(self.c):
                if self.scenario[i][j] == ".":
                    self.BFS(i, j)
                    self.colored_areas += 1
                    
        print(self.colored_areas)

    def BFS(self, x, y):
        queue = deque()
        queue.append((x, y))
        self.scenario[x][y] = "o"

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.r and 0 <= ny < self.c:
                    if self.scenario[nx][ny] == ".":
                        self.scenario[nx][ny] = "o"
                        queue.append((nx, ny))

response = Colouring_Game_Scenarios()