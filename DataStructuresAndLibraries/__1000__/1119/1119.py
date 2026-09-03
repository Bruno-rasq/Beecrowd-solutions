while True:
    N, k, m = [int(x) for x in input().split()]
    if N == 0 and k == 0 and m == 0:
        break

    circle = list(range(1, N + 1))
    visited = [False] * N

    curr1 = N - 1  # começa antes do primeiro
    curr2 = 0      # começa antes do último (vai diminuir depois)
    remainCount = N

    result = []

    while remainCount > 0:
        # Contador no sentido anti-horário (sentido crescente)
        count_k = 0
        while count_k < k:
            curr1 = (curr1 + 1) % N
            if not visited[curr1]:
                count_k += 1

        # Contador no sentido horário (sentido decrescente)
        count_m = 0
        while count_m < m:
            curr2 = (curr2 - 1 + N) % N
            if not visited[curr2]:
                count_m += 1

        if curr1 == curr2:
            result.append("%3d" % circle[curr1])
            visited[curr1] = True
            remainCount -= 1
        else:
            result.append("%3d%3d" % (circle[curr1], circle[curr2]))
            visited[curr1] = True
            visited[curr2] = True
            remainCount -= 2

    print(",".join(result))