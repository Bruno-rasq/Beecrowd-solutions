class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.head = None
        
    def add(self, value):
        self.head = self.inserir_recursivo(self.head, value)
        
    def inserir_recursivo(self, node, value):
        if node is None: return Node(value)
        if value < node.valor: node.left = self.inserir_recursivo(node.left, value)
        if value > node.valor: node.right = self.inserir_recursivo(node.right, value)
        return node
        
    def lever_order(self):
        values = []
        fila, indice = [self.head], 0
        while fila:
            size = len(fila)
            for _ in range(size):
                atual = fila.pop(0)
                values.append(str(atual.valor))
                
                if atual.left: fila.append(atual.left)
                if atual.right: fila.append(atual.right)
                
        print(" ".join(values))
    
qnt_arvores = int(input())
for i in range(1, qnt_arvores + 1):
    size = input()
    nos = [int(x) for x in input().split()]
    tree = BinaryTree()
    for no in nos:
        tree.add(no)
        
    print(f"Case {i}:")
    tree.lever_order()
    print()