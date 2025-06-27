import heapq
from collections import defaultdict

# tentando implementar o algoritmo de Prim para achar
# a arvore geradora minima do grafo em questão.
# algoritmo de prim é um algoritmo guloso que escolhe
# os menores caminhos partindo de um vertice qualquer
# e passando por todos os vertices

class Algoritmo_Prim:
    @staticmethod #-> MST minimum spanning tree
    def get_MST_weight(grafo, vertices):
        vertices_visitados = set()
        peso_total_arestas_minimas = 0
        minheap = [] 
        
        vertice_inicial = 1
        vertices_visitados.add(vertice_inicial)
        
        for vizinho, peso in grafo[vertice_inicial].items():
            heapq.heappush(minheap, (peso, vizinho))
            
        while minheap and len(vertices_visitados) < vertices:
            peso, destino = heapq.heappop(minheap)
            if destino not in vertices_visitados:
                vertices_visitados.add(destino)
                peso_total_arestas_minimas += peso 
                
                for vizinho, peso_visinho in grafo[destino].items():
                    if vizinho not in vertices_visitados:
                        heapq.heappush(minheap, (peso_visinho, vizinho))
                        
        return peso_total_arestas_minimas


class Routers:
    @staticmethod
    def resolve():
    
        vertices, arestas = [int(x) for x in input().split()]
        grafo = defaultdict(lambda: defaultdict())
        
        for _ in range(arestas):
            vertice_A, vertice_B, peso = [int(x) for x in input().split()]
            grafo[vertice_A][vertice_B] = peso
            grafo[vertice_B][vertice_A] = peso
            
        mst_weight = Algoritmo_Prim.get_MST_weight(grafo, vertices)
        print(mst_weight)
        
Routers.resolve()