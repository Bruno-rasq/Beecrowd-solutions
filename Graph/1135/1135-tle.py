class Ants_colony:
    @staticmethod
    def LCA(grafo, p, q):
        # função para calcular profundidade de um nó
        def profundidade(node):
            d = 0
            while node != grafo[node][0]:  # até raiz
                node = grafo[node][0]
                d += 1
            return d
        
        custo = 0
        
        # calcula profundidades
        dp = profundidade(p)
        dq = profundidade(q)
        
        # sobe o mais profundo até nivelar
        while dp > dq:
            custo += grafo[p][1]
            p = grafo[p][0]
            dp -= 1
        
        while dq > dp:
            custo += grafo[q][1]
            q = grafo[q][0]
            dq -= 1
        
        # agora na mesma profundidade, sobe juntos até achar comum
        while p != q:
            custo += grafo[p][1] + grafo[q][1]
            p = grafo[p][0]
            q = grafo[q][0]
        
        return custo
    
    @staticmethod
    def resolve():
        while True:
            vertices = int(input())
            if vertices == 0: break 
        
            graph = {x: [0, 0] for x in range(vertices)}
            for i in range(1, vertices):
                graph[i] = [int(x) for x in input().split()]
                
            queries = int(input())
            out = []
            for _ in range(queries):
                p, q = [int(x) for x in input().split()]
                out.append(str(Ants_colony.LCA(graph, p, q)))
                
            print(" ".join(out))
            
Ants_colony.resolve()