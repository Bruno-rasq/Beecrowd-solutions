def nova_posicao(i, N):
    mid = N // 2
    if i < mid: return i * 2 + 1
    else: return (i - mid) * 2

class Shuffle:
    @staticmethod
    def resolve ():
        n = int(input())
        i, count = 1, 1
        
        aux = nova_posicao(i, n)
        while aux != i:
            count += 1
            aux = nova_posicao(aux, n)
        print(count)
    
Shuffle.resolve()