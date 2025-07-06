import heapq
class Algorithm_Prim:
    @staticmethod
    def mst_cost(graph, vertices):
        visiteds, cost, minheap = set(), 0, []
    
        initial = 0 
        visiteds.add(initial)
        
        for neighbour, weigth in graph[initial].items():
            heapq.heappush(minheap, (weigth, neighbour))
            
        while minheap and len(visiteds) < vertices:
            weigth, target = heapq.heappop(minheap)
            if target not in visiteds:
                visiteds.add(target)
                cost += weigth
                
                for neighbour, weigth in graph[target].items():
                    if neighbour not in visiteds:
                        heapq.heappush(minheap, (weigth, neighbour))
                        
        return cost 
        
class Itinerary_of_Santa_Claus:
    @staticmethod
    def resolve():
        while True:
            vertices, arestas = [int(x) for x in input().split()]
            if vertices == arestas == 0: break
            
            graph = {vertice: {} for vertice in range(vertices)}
            for _ in range(arestas):
                vertA, vertB, weigth = [int(x) for x in input().split()]
                graph[vertA][vertB] = weigth
                graph[vertB][vertA] = weigth
                
            print(Algorithm_Prim.mst_cost(graph, vertices))
    
Itinerary_of_Santa_Claus.resolve()
