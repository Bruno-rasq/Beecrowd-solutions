class Campo_de_Minhocas:
    @staticmethod
    def solve():
        n, m = [int(x) for x in input().split()]
        campo = [[int(x) for x in input().split()] for _ in range(n)]
        col = [0] * m
        row = [0] * n
        
        for i in range(n):
            linha = campo[i]
            row[i] = sum(linha)
            for idx, n in enumerate(linha):
                col[idx] += n
                
        MAX = max(col + row)
            
        print(MAX)
            
Campo_de_Minhocas.solve()   