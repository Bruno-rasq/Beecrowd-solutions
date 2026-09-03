def contador(curr, passo, limite, visited, N):
    count = 0
    while count < limite:
        curr = (curr + passo + N) % N
        if not visited[curr]:
            count += 1
    return curr

while True:
    N, k, m = [int(x) for x in input().split()]
    if N == k == m == 0: break

    circle = list(range(1, N + 1))
    visited = [False] * N
    
    curr1 = N - 1
    curr2 = 0
    remainCount = N
    result = []
    
    while remainCount > 0:
        
        curr1 = contador(curr1, +1, k, visited, N)
        curr2 = contador(curr2, -1, m, visited, N)
    
        # Verifica se ambos chegaram na mesma posição
        if curr1 == curr2:
            result.append(f"{circle[curr1]:3d}")
            visited[curr1] = True
            remainCount -= 1
        else:
            result.append(f"{circle[curr1]:3d}{circle[curr2]:3d}")
            visited[curr1] = True
            visited[curr2] = True
            remainCount -= 2
    
    print(",".join(result))