from collections import defaultdict 

class Grafo:
    def __init__(self):
        self.qnt_vertices, self.qnt_conexoes = [
            int(x) for x in input().split()]
            
        self.grafo = defaultdict(list)
        for i in range(97, 97 + self.qnt_vertices):
            self.grafo[chr(i)] = []
    
        for _ in range(self.qnt_conexoes):
            verticeA, verticeB = input().split()
            self.grafo[verticeA].append(verticeB)
            self.grafo[verticeB].append(verticeA)
        
        self.DFSr()
        
    def DFS(self, node, visitados, conexoes):
        visitados[node] = True
        conexoes.append(node)
        for vizinho in sorted(self.grafo[node]):
            if not visitados[vizinho]:
                self.DFS(vizinho, visitados, conexoes)
        return conexoes
        
    def DFSr(self):
        visitados = {node: False for node in self.grafo}
        grupos = 0
        for node in sorted(self.grafo):  # garantir ordem
            if not visitados[node]:
                conexoes = self.DFS(node, visitados, [])
                print(",".join(sorted(conexoes)) + ",")  # ordem alfabética da componente
                grupos += 1
        print(f"{grupos} connected components")
    

class Connected_Components:
    
    @staticmethod
    def resolve():
        n = int(input())
        for i in range(1, n + 1):
            print(f"Case #{i}:")
            grafo = Grafo()
            print()  # linha em branco correta
            
Connected_Components.resolve()