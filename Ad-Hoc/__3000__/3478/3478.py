from collections import defaultdict

def DFS_iter(gp, visiteds, start, group):
    stack = [start]
    while stack:
        city = stack.pop()
        if visiteds[city] != 0:
            continue
        visiteds[city] = group
        for neighbour in gp[city]:
            if visiteds[neighbour] == 0:
                stack.append(neighbour)

class Geiapan:
    @staticmethod
    def n_of_countries_formed(cities, boundaries):
        visiteds = {i: 0 for i in range(1, cities+1)}
        
        gp = defaultdict(list)
        for _ in range(boundaries):
            a, b = map(int, input().split())
            gp[a].append(b)
            gp[b].append(a)
        
        group = 0
        for city in range(1, cities+1):
            if visiteds[city] == 0:  # ainda não visitado
                group += 1
                DFS_iter(gp, visiteds, city, group)
        
        return group
        
        
c, f = [int(x) for x in input().split()]
print(Geiapan.n_of_countries_formed(c, f))
        