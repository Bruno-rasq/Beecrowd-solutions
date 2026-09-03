from heapq import heappush, heappop


def dijkstra(graph, source, target):
    dist = {city: float("inf") for city in graph}
    parent = {city: None for city in graph}

    dist[source] = 0

    queue = [(0, source)]

    while queue:
        curr_time, city = heappop(queue)

        # Se esse valor estiver desatualizado, ignora
        if curr_time > dist[city]:
            continue

        # Chegamos ao destino com o menor tempo possível
        if city == target:
            break

        for next_city, time in graph[city]:

            new_time = curr_time + time

            if new_time < dist[next_city]:
                dist[next_city] = new_time
                parent[next_city] = city

                heappush(queue, (new_time, next_city))

    # Reconstruir caminho de trás para frente
    path = []
    city = target

    while city is not None:
        path.append(city)
        city = parent[city]

    return dist[target], path


BUFFER = ""

while True:
    n, m = [int(x) for x in input().split()]

    if n == m == 0:
        break

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        a, b, time = [int(x) for x in input().split()]

        graph[a].append((b, time))
        graph[b].append((a, time))

    target = int(input())

    minTime, path = dijkstra(graph, 1, target)

    # ELA SAI AS 5:30 E TEM 2 HORAS PARA CHEGAR À FACULDADE
    available_time = 120

    if minTime <= available_time:
        BUFFER += (
            f"Will not be late. "
            f"Travel time - {minTime} - "
            f"best way - {' '.join(map(str, path))}\n"
        )
    else:
        delay = minTime - available_time

        BUFFER += (
            f"It will be {delay} minutes late. "
            f"Travel time - {minTime} - "
            f"best way - {' '.join(map(str, path))}\n"
        )

print(BUFFER, end="")