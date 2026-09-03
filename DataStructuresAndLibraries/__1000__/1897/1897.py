from collections import deque

def trunc_div(a, b):
    # Divisão inteira truncada em direção a zero (como em C++)
    if b == 0:
        return 0  # só por segurança, mas no problema não acontece
    return a // b if a >= 0 else -((-a) // b)

def bfs(n, n2):
    if n == n2:
        return 0
    
    q = deque([(n, 0)])
    visited = set()
    
    while q:
        u, steps = q.popleft()
        if u == n2:
            return steps
        if u in visited:
            continue
        visited.add(u)

        # mesmas operações do código C++
        q.append((u * 2, steps + 1))
        q.append((u * 3, steps + 1))
        q.append((trunc_div(u, 2), steps + 1))
        q.append((trunc_div(u, 3), steps + 1))
        q.append((u + 7, steps + 1))
        q.append((u - 7, steps + 1))
    
    return -1  # se não encontrar (em tese, sempre encontra)

class Smart_Game_1897:
    @staticmethod
    def solve():
        n, n2 = map(int, input().split())
        print(bfs(n, n2)) 
        
Smart_Game_1897.solve()