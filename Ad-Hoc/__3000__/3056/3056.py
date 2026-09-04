class Ponto_do_Meio:
    @staticmethod
    def solve():
        passos = int(input())
        nodes = 2 
        for _ in range(passos):
            nodes += nodes - 1
           
        print(nodes * nodes)
        
Ponto_do_Meio.solve()