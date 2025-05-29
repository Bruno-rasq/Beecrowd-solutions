def minimum_swaps_to_sort(arr):
    n = len(arr)
    visited = [False] * n
    # Pares de (valor, índice original)
    arr_pos = list(enumerate(arr))
    arr_pos.sort(key=lambda x: x[1])  # Ordenar com base no valor

    swaps = 0
    for i in range(n):
        if visited[i] or arr_pos[i][0] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += (cycle_size - 1)
    
    return swaps


# ==== Leitura dos testes ====
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # Corrigir índice para começar em 0
    arr = [x - 1 for x in arr]  # Permutação de 0 a N-1
    print(minimum_swaps_to_sort(arr))