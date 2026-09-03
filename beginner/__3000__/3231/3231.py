"""
    HI:

    se o filme(id) estiver na lista -> Hi == 0
    se não tem similaridade com nenhum filme da lista -> HI = INFINITO
    do contrário -> HI = distância que o filme tem de um filme da lista.
    
"""

import sys
input = sys.stdin.buffer.readline

INFINIT = float('inf')
n, h, l = map(int, input().split())
horror_list = map(int, input().split())
graph = {id: [] for id in range(n) }

for _ in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = []
dist = [INFINIT for _ in range(n)]
for id in horror_list:
    queue.append(id)
    dist[id] = 0

head = 0
while head < len(queue):
    curr = queue[head]
    head += 1
    for v in graph[curr]:
        if dist[v] == INFINIT:
            dist[v] = dist[curr] + 1
            queue.append(v)

maxH = max(dist)

for id in range(n):
    if dist[id] == maxH:
        print(id)
        break