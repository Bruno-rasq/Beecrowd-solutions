class Node:
    def __init__(self, nome, left=None, right=None):
        self.nome = nome
        self.left = left
        self.right = right
        
times = [int(x) for x in input().split()]

oitavas_1 = Node("oitavas", Node(times[0]), Node(times[1]))
oitavas_2 = Node("oitavas", Node(times[2]), Node(times[3]))
quartas_1 = Node("quartas", oitavas_1, oitavas_2)

oitavas_3 = Node("oitavas", Node(times[4]), Node(times[5]))
oitavas_4 = Node("oitavas", Node(times[6]), Node(times[7]))
quartas_2 = Node("quartas", oitavas_3, oitavas_4)

semi_1 = Node("semifinal", quartas_1, quartas_2)

oitavas_5 = Node("oitavas", Node(times[8]), Node(times[9]))
oitavas_6 = Node("oitavas", Node(times[10]), Node(times[11]))
quartas_3 = Node("quartas", oitavas_5, oitavas_6)

oitavas_7 = Node("oitavas", Node(times[12]), Node(times[13]))
oitavas_8 = Node("oitavas", Node(times[14]), Node(times[15]))
quartas_4 = Node("quartas", oitavas_7, oitavas_8)

semi_2 = Node("semifinal", quartas_3, quartas_4)

final = Node("final", semi_1, semi_2)


class Copa:
    @staticmethod
    def find_LCA(root, t1, t2):
        if root is None:
            return None
        
        # Se achamos um dos times (folhas)
        if root.nome == t1 or root.nome == t2:
            return root
        
        # Busca nos dois lados
        left = Copa.find_LCA(root.left, t1, t2)
        right = Copa.find_LCA(root.right, t1, t2)
        
        # Se achou nos dois lados, então esse nó é o LCA
        if left and right:
            return root
        
        # Se achou só em um lado, propaga
        return left if left else right
    
    @staticmethod
    def resolve():
        lca = Copa.find_LCA(final, 1, 9)
        
        print(lca.nome)

Copa.resolve()