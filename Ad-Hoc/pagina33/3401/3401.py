import math
class Guava_Bug_Attacks_Again:
    @staticmethod
    def resolve():
        
        n_trees, bug_jump_size = [int(x) for x in input().split()]
        
        coords = Guava_Bug_Attacks_Again.set_coord(n_trees)
        adj = Guava_Bug_Attacks_Again.set_table_adj(coords, bug_jump_size)
        Guava_Bug_Attacks_Again.DFS(adj, n_trees)
        
        
    @staticmethod #-> O(N)
    def set_coord(n_trees: int):
        coords = []
        for _ in range(n_trees):
            x, y = [int(x) for x in input().split()]
            coords.append((x, y))
        return coords
        
    @staticmethod #-> O(n²) + O(n²)
    def set_table_adj(coords, size_jump):
        L = len(coords)
        adj = [[0] * L for _ in range(L)]
        for i in range(L):
            xi, yi = coords[i]
            for j in range(L):
                if i == j: continue #mesmo nó, distância zero 
                xj, yj = coords[j]
                
                dist = math.hypot(xi - xj, yi - yj)
                if dist <= size_jump:
                    adj[i][j] = 1 
        return adj
        
    @staticmethod
    def DFS(adj, n_trees):
        
        visiteds = [False] * n_trees
        stack = [0]
        visiteds[0] = True
        
        while stack:
            u = stack.pop()
            for v in range(n_trees):
                if adj[u][v] and not visiteds[v]:
                    visiteds[v] = True
                    stack.append(v)
        
        print("S" if all(visiteds) else "N")
        
Guava_Bug_Attacks_Again.resolve()