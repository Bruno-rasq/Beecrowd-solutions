source, target, n = map(int, input().split())
nums = list(map(int, input().split()))

LIMIT = 100000

def BFS(source, target):
    if source == target:
        return 0

    visited = [False] * (LIMIT + 1)
    visited[source] = True

    queue = [(source, 0)]
    head = 0

    while head < len(queue):
        value, operations = queue[head]
        head += 1

        if value == target:
            return operations

        for num in nums:

            # Soma
            x = value + num
            if 1 <= x <= LIMIT and not visited[x]:
                if x == target:
                    return operations + 1
                visited[x] = True
                queue.append((x, operations + 1))

            # Subtração
            x = value - num
            if 1 <= x <= LIMIT and not visited[x]:
                if x == target:
                    return operations + 1
                visited[x] = True
                queue.append((x, operations + 1))

            # Multiplicação
            x = value * num
            if 1 <= x <= LIMIT and not visited[x]:
                if x == target:
                    return operations + 1
                visited[x] = True
                queue.append((x, operations + 1))

            # Divisão
            if num != 0 and value % num == 0:
                x = value // num
                if 1 <= x <= LIMIT and not visited[x]:
                    if x == target:
                        return operations + 1
                    visited[x] = True
                    queue.append((x, operations + 1))

    return -1


print(BFS(source, target))