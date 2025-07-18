from collections import deque 

class Rambo_s_Hideout:
    
    @staticmethod
    def BFS(GP, pi):
        visiteds = set()
        visiteds.add(pi)
        queue = deque([pi])
        
        while queue:
            node = queue.popleft()
            for next_node in GP[node]:
                if next_node not in visiteds:
                    visiteds.add(next_node)
                    queue.append(next_node)
                    
        return visiteds
    
    @staticmethod
    def resolve():
        vertices, arestas = [int(x) for x in input().split()]
        GP = {vertice: [] for vertice in range(vertices)}
        
        for _ in range(arestas):
            verticeA, verticeB = [int(x) for x in input().split()]
            GP[verticeA].append(verticeB)
            GP[verticeB].append(verticeA)
        
        # BFS para verificar conectividade
        visitados = Rambo_s_Hideout.BFS(GP, 0)
        
        # Verifica se todos os vértices com grau > 0 foram visitados
        for v in range(vertices):
            if len(GP[v]) > 0 and v not in visitados:
                print("Rambo esta perdido")
                return
        
        # Verifica se todos os vértices têm grau par
        for v in range(vertices):
            if len(GP[v]) % 2 != 0:
                print("Rambo esta perdido")
                return
        
        print("Rambo esta salvo")
            
Rambo_s_Hideout.resolve()