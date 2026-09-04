import sys
readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())
cycle = [7, 9, 3, 1]

for _ in range(n):
    k = int(readline())
    write(f"{cycle[(k - 1) % 4]}\n")