import heapq

n = int(input())
tubos = [int(x) for x in input().split()]

## implementacao com uma min-heap
heapq.heapify(tubos)

ans = 0

while len(tubos) > 1:
    a = heapq.heappop(tubos)
    b = heapq.heappop(tubos)

    novo = a + b
    ans += novo

    heapq.heappush(tubos, novo)

print(ans)