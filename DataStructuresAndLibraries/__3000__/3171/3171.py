class Graph:
    def __init__(self):
        self.grap = {}
        self.visitados = set()
    
    def add(self, n, m):
        if n not in self.grap:
            self.grap[n] = []
        if m not in self.grap:
            self.grap[m] = []
        self.grap[n].append(m)
        self.grap[m].append(n)
        
    def DFS(self, node):
        self.visitados.add(node)
        for vizinho in self.grap[node]:
            if vizinho not in self.visitados:
                self.DFS(vizinho)

while True:
    try:
        N_leds, N_segmentos = [int(x) for x in input().split()]
        
        graph = Graph()
        
        for _ in range(N_segmentos):
            N, M = [int(x) for x in input().split()]
            graph.add(N, M)

        # Começa a busca do nó 1
        graph.DFS(1)

        conectado = len(graph.visitados) == N_leds
        print("COMPLETO" if conectado else "INCOMPLETO")
    except EOFError:
        break