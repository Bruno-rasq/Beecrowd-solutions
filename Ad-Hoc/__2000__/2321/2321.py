class Detectando_Colisões:
    @staticmethod
    def resolve():
        xa0, ya0, xa1, ya1 = [int(x) for x in input().split()]
        xb0, yb0, xb1, yb1 = [int(x) for x in input().split()]
        
        collid = not (xa1 < xb0 or xb1 < xa0 or ya1 < yb0 or yb1 < ya0)
        
        print(1 if collid else 0)
        
Detectando_Colisões.resolve()