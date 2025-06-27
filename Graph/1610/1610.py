class Graph:
    @staticmethod
    def has_cycle(gp):
        WHITE, GRAY, BLACK = 0, 1, 2
        STATES = {node: WHITE for node in gp}
        
        def DFS(node):
            STATES[node] = GRAY
            for v in gp[node]:
                if STATES[v] == WHITE:
                    if DFS(v): return True
                elif STATES[v] == GRAY:
                    return True
            STATES[node] = BLACK
            return False
        
        for node in gp:
            if STATES[node] == WHITE:
                if DFS(node): return True
        return False

class Dudu_Service_Maker:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            vertices, arestas = [int(x) for x in input().split()]
            GP = {node: [] for node in range(1, vertices + 1)}
            
            for _ in range(arestas):
                verticeA, verticeB = [int(x) for x in input().split()]
                GP[verticeA].append(verticeB)
                
            print("SIM" if Graph.has_cycle(GP) else "NAO")
            
Dudu_Service_Maker.resolve()