from collections import defaultdict

class DesignLabirt:
    def __init__(self):
        self.grid = defaultdict(list)
        self.node_start = int(input())
        self.size, self.n = [int(x) for x in input().split()]
        
        for _ in range(self.n):
            node, con = [int(x) for x in input().split()]
            self.grid[node].append(con)
            self.grid[con].append(node)  # adiciona nas duas direções
        
    def exibir(self):
        arestas_unicas = set()
        
        for node in self.grid:
            for vizinho in self.grid[node]:
                aresta = tuple(sorted([node, vizinho]))
                arestas_unicas.add(aresta)
        
        print(len(arestas_unicas) * 2)

class Solucao:
    @staticmethod
    def resolve():
        n_casos_teste = int(input())    
        for _ in range(n_casos_teste):
            sol = DesignLabirt()
            sol.exibir()

Solucao.resolve()