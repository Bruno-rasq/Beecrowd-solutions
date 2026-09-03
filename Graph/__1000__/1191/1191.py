import sys

class Ordered_Tree:
    @staticmethod
    def posfixa(preord, inord):
        if not preord:
            return ""
        
        root = preord[0]
        root_idx_in = inord.index(root)
        
        sub_left_in = inord[:root_idx_in]
        sub_right_in = inord[root_idx_in + 1:]
        sub_left_pre = preord[1: 1 + len(sub_left_in)]
        sub_right_pre = preord[1 + len(sub_left_in):]
        
        left_pos = Ordered_Tree.posfixa(sub_left_pre, sub_left_in)
        right_pos = Ordered_Tree.posfixa(sub_right_pre, sub_right_in)
        
        return left_pos + right_pos + root
        
class Tree_Recovery:
    @staticmethod
    def resolve():
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                preord, inord = line.split()
                posord = Ordered_Tree.posfixa(preord, inord)
                print(posord)
            except ValueError:
                # Caso a linha não tenha duas palavras corretamente
                continue

Tree_Recovery.resolve()