MAX = 20

disc = [False] * MAX
graph = [[0] * MAX for _ in range(MAX)]

def clean(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = 0
        disc[i] = False

def dfs(v, n, s):
    path = False
    disc[v] = True

    for i in range(n):
        if graph[v][i] == 1:
            path = True
            print(" " * s, end='')
            if not disc[i]:
                print(f"{v}-{i} pathR(G,{i})")
                dfs(i, n, s + 2)
            else:
                print(f"{v}-{i}")
    
    return path

def dfs_runner(v):
    ind = 0

    while True:
        if dfs(ind, v, 2):
            print()  # linha em branco

        ind = -1
        for i in range(v):
            if not disc[i]:
                ind = i
                break

        if ind == -1:
            break

def main():
    n = int(input())
    c = 1

    for _ in range(n):
        v, e = map(int, input().split())
        clean(v)

        for _ in range(e):
            o, d = map(int, input().split())
            graph[o][d] = 1

        print(f"Caso {c}:")
        c += 1
        dfs_runner(v)


main()