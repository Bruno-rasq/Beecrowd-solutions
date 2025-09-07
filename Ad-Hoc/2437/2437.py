class Distancia_de_Manhattan:
    @staticmethod
    def solve():
        XA, YA, XB, YB = [int(x) for x in input().split()]
        print(abs(XA - XB) + abs(YA - YB))
        
Distancia_de_Manhattan.solve()