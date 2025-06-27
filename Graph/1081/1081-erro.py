class Grafo:
    def __init__(self, k_nodes, k_arrestas):
        self.grafo = {node: [] for node in range(k_nodes)}
        for _ in range(k_arrestas):
            u, v = map(int, input().split())
            self.grafo[u].append(v)
        for node in self.grafo:
            self.grafo[node].sort()

    def DFS(self, u, visitados, nivel):
        visitados[u] = True
        for v in self.grafo[u]:
            if not visitados[v]:
                print(" " * nivel + 
                f"{u}-{v} pathR(G,{v})")
                self.DFS(v, visitados, nivel + 2)
            else:
                print(" " * nivel + 
            f"{u}-{v}")

    def DFSr(self):
        visitados = [False] * len(self.grafo)
        for u in range(len(self.grafo)):
            if not visitados[u]:
                self.DFS(u, visitados, 2)

class Depth_Hierarchy:
    @staticmethod
    def resolve():
        n = int(input())
        for caso in range(1, n + 1):
            k_nodes, k_arrestas = map(int, input().split())
            grafo = Grafo(k_nodes, k_arrestas)
            print(f"Caso {caso}:")
            grafo.DFSr()
            print()
            
Depth_Hierarchy.resolve()