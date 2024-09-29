class No:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, data):
        node = No(data)  # Corrigido para usar No
        if self.root is None:
            self.root = node
            self.count += 1
        else:
            self._search_node(self.root, node)

    def search(self, data):
        found = self._search_node_data(self.root, data)
        if found:
            print(f"{data} existe")
        else:
            print(f"{data} nao existe")

    def _search_node_data(self, current, data):
        if current is None:
            return False
        if data < current.data:
            return self._search_node_data(current.left, data)
        elif data > current.data:
            return self._search_node_data(current.right, data)
        return True

    def _search_node(self, current, node):
        if node.data < current.data:
            if current.left is None:
                current.left = node
                self.count += 1
            else:
                self._search_node(current.left, node)
        elif node.data > current.data:
            if current.right is None:
                current.right = node
                self.count += 1
            else:
                self._search_node(current.right, node)

    def in_order(self):
        nodelist = []
        self._traverse_in_order(self.root, nodelist)
        print(" ".join(nodelist))

    def _traverse_in_order(self, current, nodelist):
        if current:
            self._traverse_in_order(current.left, nodelist)
            nodelist.append(str(current.data))  # Convertendo para string
            self._traverse_in_order(current.right, nodelist)

    def pre_order(self):
        nodelist = []
        self._traverse_pre_order(self.root, nodelist)
        print(" ".join(nodelist))

    def _traverse_pre_order(self, current, nodelist):
        if current:
            nodelist.append(str(current.data))  # Convertendo para string
            self._traverse_pre_order(current.left, nodelist)
            self._traverse_pre_order(current.right, nodelist)

    def pos_order(self):
        nodelist = []
        self._traverse_pos_order(self.root, nodelist)
        print(" ".join(nodelist))

    def _traverse_pos_order(self, current, nodelist):
        if current:
            self._traverse_pos_order(current.left, nodelist)
            self._traverse_pos_order(current.right, nodelist)
            nodelist.append(str(current.data))  # Convertendo para string

bst = BST()
while True:
    try:
        curr = input()

        if curr == "INFIXA":
            bst.in_order()

        elif curr == "POSFIXA":
            bst.pos_order()

        elif curr == "PREFIXA":
            bst.pre_order()

        else:
            action, data = curr.split(" ")

            if action == "P":
                bst.search(data)

            else:
                bst.add(data)

    except EOFError:
        break
