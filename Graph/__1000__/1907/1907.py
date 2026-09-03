import sys

data = sys.stdin.buffer.read().splitlines()

n, m = map(int, data[0].split())

W = m + 2
H = n + 2

# '#' = 35
# '.' = 46
# 'o' = 111

grid = bytearray(b'#' * (W * H))

for i in range(n):
    ini = (i + 1) * W + 1
    grid[ini:ini + m] = data[i + 1]

areas = 0

for r in range(1, n + 1):
    base = r * W
    for c in range(1, m + 1):
        idx = base + c

        if grid[idx] == 46:
            areas += 1
            grid[idx] = 111

            queue = [idx]
            head = 0
            append = queue.append

            while head < len(queue):
                p = queue[head]
                head += 1

                q = p - W
                if grid[q] == 46:
                    grid[q] = 111
                    append(q)

                q = p + W
                if grid[q] == 46:
                    grid[q] = 111
                    append(q)

                q = p - 1
                if grid[q] == 46:
                    grid[q] = 111
                    append(q)

                q = p + 1
                if grid[q] == 46:
                    grid[q] = 111
                    append(q)

print(areas)