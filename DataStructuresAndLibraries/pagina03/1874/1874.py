from collections import deque

class Solucao:
    def __init__(self, n, m, k):
        self.matrix = []
        self.void_blocks = []
        self.queue = deque()
        self.set_matrix_and_voidblocks(n, m)
        self.set_queue(k)
        
    def set_matrix_and_voidblocks(self, n, m):
        #matrix organizada por colunas
        for i in range(n):
            line = input().split()
            self.matrix.append(line)
            for j in range(m):
                if line[j] == "0": 
                    self.void_blocks.append((i, j))

    def set_queue(self, k):
        nums = input().split()
        for i in range(k):
            self.queue.append(nums[i])
        
    def pushing_blocks(self):
        lista_ordenada = sorted(
            self.void_blocks, 
            key=lambda tupla: (tupla[1], tupla[0]), 
            reverse=True
        )
        while len(self.queue) > 0 and len(lista_ordenada) > 0:
            n = self.queue.popleft()
            i, j = lista_ordenada.pop(0)
            self.matrix[i][j] = n
            
    def get(self):
        self.pushing_blocks()
        for line in self.matrix:
            print(" ".join(line))


while True:
    n, m, k = [int(x) for x in input().split()]
    if n == m == k == 0: break
    
    solucao = Solucao(n, m, k)
    solucao.get()