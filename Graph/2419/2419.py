class Solucao:
    def __init__(self):
        self.n, self.m = [int(x) for x in input().split()]
        self.mapa = [input() for _ in range(self.n)]  # Agora cada linha é uma string
        self.direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
    def calc_extensao_territorial_costa(self):
        extensao_territorial = 0
        
        for row in range(self.n):
            for col in range(self.m):
                if self.mapa[row][col] == "#":
                    for dr, dc in self.direcoes:
                        nr, nc = row + dr, col + dc
                        if not (0 <= nr < self.n and 0 <= nc < self.m) or self.mapa[nr][nc] == ".":
                            extensao_territorial += 1
                            break  # conta uma vez só
        print(extensao_territorial)

sol = Solucao()
sol.calc_extensao_territorial_costa()