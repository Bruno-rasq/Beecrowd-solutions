"""
    adaptação do problema do carteiro chinês (CPP)
    chinese postman problem.
    
    a ideia é visitar todos os vertices partindo de um
    ponto inicial e terminando no mesmo. para isso aplico
    o algoritmo de Prim para encontrar a árvore geradora
    minima (MST -> minimum spanning tree) o resultado é
    a somatoria dos custos das arestas * 2
    
"""

import heapq
from collections import defaultdict 

class MST:  # Algoritmo de Prim
    @staticmethod
    def sigma_weight(graph, start):
        visited = set()
        minheap = []
        total_mst_cost = 0
        
        visited.add(start)
        for neighbour, weight in graph[start].items():
            heapq.heappush(minheap, (weight, neighbour))
        
        # Enquanto não visitarmos todos os vértices
        while minheap and len(visited) < len(graph):
            weight, target = heapq.heappop(minheap)
            if target not in visited:
                visited.add(target)
                total_mst_cost += weight
                
                for next_neighbour, next_weight in graph[target].items():
                    if next_neighbour not in visited:
                        heapq.heappush(minheap, (next_weight, next_neighbour))
        
        # O custo final do circuito = 2 * custo da MST
        return total_mst_cost * 2
        
class G_of_graph:
    @staticmethod
    def resolve():
        n_vertices, n_edges = [int(x) for x in input().split()]
        PI = int(input())
        graph = defaultdict(lambda: defaultdict())
        
        for _ in range(n_edges):
            verticeA, verticeB, weight = [int(x) for x in input().split()]
            graph[verticeA][verticeB] = weight
            graph[verticeB][verticeA] = weight
            
        out = MST.sigma_weight(graph, PI)
        print(out)
        
G_of_graph.resolve()