# classficacao:
# pre_order: Raiz, sub esquerda, sub direita.
# in_order: sub esquerda, Raiz, sub direita.
# pos_order: sub esquerda, sub direira, Raiz.

# para achar a raiz basta pegar o primeiro elemento
# na formação pre_order, depois disso para saber as
# sub árvores esquerda e direita basta pegar os elementos
# á esquerda e direita da raiz no forma in_order.

class Pos_order:
    @staticmethod
    def get(pre_order: str, in_order: str) -> str:
        # Condição de parada
        if not pre_order: return ""
        
        # Raiz é o primeiro elemento do pré-ordem
        root = pre_order[0]
        root_index_in = in_order.index(root)
        
        # Subárvore esquerda e direita (in-ordem)
        in_esq = in_order[:root_index_in]
        in_dir = in_order[root_index_in + 1:]

        # Subárvore esquerda e direita (pré-ordem)
        # Pegamos o mesmo número de elementos que há na subárvore esquerda
        pre_esq = pre_order[1:1 + len(in_esq)]
        pre_dir = pre_order[1 + len(in_esq):]

        # Recursão
        left_post = Pos_order.get(pre_esq, in_esq)
        right_post = Pos_order.get(pre_dir, in_dir)

        return left_post + right_post + root
        
        
class Pre_In_and_Post:
    @staticmethod
    def resolve():
        n = int(input())
        for _ in range(n):
            nodes, pre_order, in_order = input().split()
            pos_order = Pos_order.get(pre_order, in_order)
            print(pos_order)
            
Pre_In_and_Post.resolve()