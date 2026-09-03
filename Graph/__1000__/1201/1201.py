def max_node(node):
    curr = node
    while curr.right is not None:
        curr = curr.right
    return curr

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST: #-> Binary Seaching Tree
    def __init__(self): self.root = None
    
    def infix(self): 
        vals = []
        self.infix_rec(self.root, vals)
        print(" ".join(vals))
    def infix_rec(self, node, vals):
        if node:
            self.infix_rec(node.left, vals)
            vals.append(str(node.val))
            self.infix_rec(node.right, vals)
            
    def prefix(self):
        vals = []
        self.prefix_rec(self.root, vals)
        print(" ".join(vals))
    def prefix_rec(self, node, vals):
        if node:
            vals.append(str(node.val))
            self.prefix_rec(node.left, vals)
            self.prefix_rec(node.right, vals)
            
    def posfix(self): 
        vals = []
        self.posfix_rec(self.root, vals)
        print(" ".join(vals))
    def posfix_rec(self, node, vals):
        if node:
            self.posfix_rec(node.left, vals)
            self.posfix_rec(node.right, vals)
            vals.append(str(node.val))
    
    def insert(self, valor):self.root = self.add_rec(self.root, valor)
    def add_rec(self, node, valor):
        if node is None: return Node(valor)
        elif valor < node.val: node.left = self.add_rec(node.left, valor)
        elif valor > node.val: node.right = self.add_rec(node.right, valor)
        return node
        
    def search(self, valor): self.search_rec(self.root, valor)
    def search_rec(self, node, valor):
        if node is None: print(f"{valor} nao existe")
        elif node.val == valor: print(f"{valor} existe")
        elif valor < node.val: self.search_rec(node.left, valor)
        elif valor > node.val: self.search_rec(node.right, valor)
        
    
    def remove(self, valor): self.root = self.remove_rec(self.root, valor)
    def remove_rec(self, node, valor):
        if node is None: return None
        elif valor < node.val: node.left = self.remove_rec(node.left, valor)
        elif valor > node.val: node.right = self.remove_rec(node.right, valor)
        else:
            # CASO 1: sem filhos
            if node.left is None and node.right is None: return None
            # CASO 2: um filho
            elif node.left is None: return node.right
            elif node.right is None: return node.left
            # CASO 3: dois filhos
            else:
                antecessor = max_node(node.left)
                node.val = antecessor.val
                node.left = self.remove_rec(node.left, antecessor.val)
        return node
    
class BST_Operations_II:
    @staticmethod
    def resolve():
        bst = BST()
        while True:
            try:
                request = input()
                parts = request.split()
                    
                if len(parts) == 2:
                    if parts[0] == "I": bst.insert(int(parts[1]))
                    if parts[0] == "P": bst.search(int(parts[1]))
                    if parts[0] == "R": bst.remove(int(parts[1]))
                    
                if request == "INFIXA": bst.infix()
                if request == "PREFIXA": bst.prefix()
                if request == "POSFIXA": bst.posfix()
            except EOFError: break 
        
BST_Operations_II.resolve()