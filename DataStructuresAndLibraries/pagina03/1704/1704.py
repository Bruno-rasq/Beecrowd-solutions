#utiliza priority queue

import heapq

while True:
    try:
        n, h = map(int, input().split())
        tarefas_por_prazo = [[] for _ in range(h + 1)]
        total = 0

        for _ in range(n):
            valor, prazo = map(int, input().split())
            tarefas_por_prazo[prazo].append(valor)
            total += valor

        heap = []
        ganhos = 0

        # Começa da última hora até a primeira
        for hora in range(h, 0, -1):
            for valor in tarefas_por_prazo[hora]:
                heapq.heappush(heap, -valor)  # max-heap com valores negativos

            if heap:
                ganhos += -heapq.heappop(heap)  # pega a tarefa mais valiosa

        print(total - ganhos)

    except EOFError:
        break