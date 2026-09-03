from collections import deque

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prev = None
        self.next = None
        
class BinaryTree:
    def __init__(self, nodes: list[int]):
        self.head = None
        for node in nodes:
            self.inserir(node)
        
    def inserir(self, valor):
        self.head = self._inserir_recursivo(self.head, valor)

    def _inserir_recursivo(self, node, valor):
        if node is None: return Node(valor)
        if valor < node.valor: node.prev = self._inserir_recursivo(node.prev, valor)
        if valor > node.valor: node.next = self._inserir_recursivo(node.next, valor)
        return node

    def exibir_por_camadas(self):
        fila, indice = deque([self.head]), 0
        
        while fila:
            nivel_tamanho = len(fila)
            nivel_valores = []
            
            for _ in range(nivel_tamanho):
                atual = fila.popleft()
                nivel_valores.append(atual.valor)
                
                if atual.prev: fila.append(atual.prev)
                if atual.next: fila.append(atual.next)
                
            print(f"{indice} {min(nivel_valores)}")
            indice += 1

n = int(input())
nodes = [int(x) for x in input().split()]
tree = BinaryTree(nodes)
tree.exibir_por_camadas()