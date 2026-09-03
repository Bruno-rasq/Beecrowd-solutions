from collections import defaultdict, deque

class The_Rat_in_a_Maze:
    @staticmethod
    def BFS(pi: str, target: str, GP):
        if pi == target: return 0
        
        visites = set()
        visites.add(pi)
        queue = deque([(pi, 0)])
        
        while queue:
            node, point = queue.popleft()
            for next_node in GP[node]:
                if next_node == target: return point + 1
                if next_node not in visites:
                    visites.add(next_node)
                    queue.append((next_node, point + 1))

        return 0
    
    @staticmethod
    def resolve():
        amount_nodes, amount_links = [int(x) for x in input().split()]
        
        GP = defaultdict(list)
        for _ in range(amount_links):
            nodeA, nodeB = input().split()
            GP[nodeA].append(nodeB)
            GP[nodeB].append(nodeA)
            
        left = The_Rat_in_a_Maze.BFS("Entrada", "*", GP)
        right = The_Rat_in_a_Maze.BFS("*", "Saida", GP)
        
        print(left + right)
        
The_Rat_in_a_Maze.resolve()