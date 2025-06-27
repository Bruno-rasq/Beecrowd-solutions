class Node:
    def __init__(self, char):
        self.char = char
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
            vals.append(node.char)
            self.infix_rec(node.right, vals)
            
    def prefix(self):
        vals = []
        self.prefix_rec(self.root, vals)
        print(" ".join(vals))
    def prefix_rec(self, node, vals):
        if node:
            vals.append(node.char)
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
            vals.append(node.char)
    
    def insert(self, char):self.root = self.add_rec(self.root, char)
    def add_rec(self, node, char):
        if node is None: return Node(char)
        elif ord(char) < ord(node.char): node.left = self.add_rec(node.left, char)
        elif ord(char) > ord(node.char): node.right = self.add_rec(node.right, char)
        return node
        
    def search(self, char): self.search_rec(self.root, char)
    def search_rec(self, node, char):
        if node is None: print(f"{char} nao existe")
        elif node.char == char: print(f"{char} existe")
        elif ord(char) < ord(node.char): self.search_rec(node.left, char)
        elif ord(char) > ord(node.char): self.search_rec(node.right, char)
        
class BST_Operations_I:
    @staticmethod
    def resolve():
        bst = BST()
        while True:
            try:
                request = input()
                parts = request.split()
                    
                if len(parts) == 2:
                    if parts[0] == "I": bst.insert(parts[1])
                    if parts[0] == "P": bst.search(parts[1])
                    
                if request == "INFIXA": bst.infix()
                if request == "PREFIXA": bst.prefix()
                if request == "POSFIXA": bst.posfix()
            except EOFError: break 
        
BST_Operations_I.resolve()