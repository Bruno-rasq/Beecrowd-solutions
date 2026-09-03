# Solucao implementa uma verificação simplificada
# do funcionamento do algoritmo de Korasaju
# algoritmo Korasaj -> O(N + E) e tem como um dos casos
# de uso a verificação de que o grafo é fortemente 
# conectado.

from collections import defaultdict

class Grafo:
    def __init__(self, n_vertices, m_arestas): #-> O(N)
        self.vertices = n_vertices + 1  # considerando vértices de 1 até N
        self.grafo = defaultdict(list)
        self.grafo_rev = defaultdict(list)
        
        for _ in range(m_arestas):
            verticeA, verticeB, con = map(int, input().split())
            
            self.grafo[verticeA].append(verticeB)
            self.grafo_rev[verticeB].append(verticeA)
            
            if con == 2:  # ligação dupla
                self.grafo[verticeB].append(verticeA)
                self.grafo_rev[verticeA].append(verticeB)
                
    def DFS(self, node, visitados, grafo): #-> O(V + E)
        visitados[node] = True
        for vizinho in grafo[node]:
            if not visitados[vizinho]:
                self.DFS(vizinho, visitados, grafo)
                
    def e_fortemente_conectado(self): #O(V + E)
        visitados = [False] * self.vertices
        self.DFS(1, visitados, self.grafo)  # começa do vértice 1
        if not all(visitados[1:]): return 0
        
        visitados = [False] * self.vertices
        self.DFS(1, visitados, self.grafo_rev)
        if not all(visitados[1:]): return 0

        return 1

class Come_and_Go:
    @staticmethod
    def resolve(): #-> O(M)
        while True:
            n_vertices, m_arestas = map(int, input().split())
            if n_vertices == m_arestas == 0: break
            
            grafo = Grafo(n_vertices, m_arestas)
            print(grafo.e_fortemente_conectado())

Come_and_Go.resolve()