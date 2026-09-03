import sys

class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    cur = root
    while True:
        if value < cur.key:
            if cur.left is None:
                cur.left = Node(value)
                break
            cur = cur.left
        elif value > cur.key:
            if cur.right is None:
                cur.right = Node(value)
                break
            cur = cur.right
        else:
            break

    return root


def prefix(node, vals):
    if node is None:
        return

    append = vals.append

    def dfs(n):
        if n:
            append(str(n.key))
            dfs(n.left)
            dfs(n.right)

    dfs(node)


def infix(node, vals):
    if node is None:
        return

    append = vals.append

    def dfs(n):
        if n:
            dfs(n.left)
            append(str(n.key))
            dfs(n.right)

    dfs(node)


def postfix(node, vals):
    if node is None:
        return

    append = vals.append

    def dfs(n):
        if n:
            dfs(n.left)
            dfs(n.right)
            append(str(n.key))

    dfs(node)


tokens = sys.stdin.read().split()
it = iter(tokens)

C = int(next(it))
out = []
out_append = out.append

for case in range(1, C + 1):
    N = int(next(it))

    root = None
    for _ in range(N):
        root = insert(root, int(next(it)))

    out_append(f"Case {case}:\n")

    vals = []
    prefix(root, vals)
    out_append("Pre.: " + " ".join(vals) + "\n")

    vals = []
    infix(root, vals)
    out_append("In..: " + " ".join(vals) + "\n")

    vals = []
    postfix(root, vals)
    out_append("Post: " + " ".join(vals) + "\n\n")

sys.stdout.write("".join(out))