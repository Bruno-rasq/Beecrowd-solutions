from collections import deque

class Help_Clotilde:
    @staticmethod
    def next_channels(pi: int, target: int, banned_channels: set[int]):
        LIMIT, adj = 10**5, []
        
        A,B,C,D,E = pi + 1, pi * 2, pi * 3, pi - 1, pi // 2
        if A <= LIMIT and A not in banned_channels: adj.append(A)
        if B <= LIMIT and B not in banned_channels: adj.append(B)
        if C <= LIMIT and C not in banned_channels: adj.append(C)
        if D >= 1 and D not in banned_channels: adj.append(D)
        if pi % 2 == 0 and E >= 1 and E not in banned_channels: adj.append(E)
    
        return adj
            
    @staticmethod
    def BFS(pi: int, target: int, banned_channels: list[int]):
        if pi == target: return 0
        
        visiteds = set()
        visiteds.add(pi)
        queue = deque([(pi, 0)]) #-> channel, clicks 
        
        while queue:
            curr, clicks = queue.popleft()
            
            for next_channel in Help_Clotilde.next_channels(curr, target, banned_channels):
                if next_channel == target: return clicks + 1
                if next_channel not in visiteds:
                    visiteds.add(next_channel)
                    queue.append([next_channel, clicks + 1])
                    
        return None #caso seja impossível 
            
    @staticmethod
    def resolve():
        while True:
            entrada = [int(x) for x in input().strip().split()]
            if entrada == [0, 0, 0]: break
        
            banned_channels = [int(x) for x in input().strip().split()]
            
            clicks = Help_Clotilde.BFS(entrada[0], entrada[1], banned_channels)
            print(clicks if clicks != None else -1)
    
Help_Clotilde.resolve()  