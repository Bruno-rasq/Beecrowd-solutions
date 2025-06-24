class Colision:
    @staticmethod #-> O(N)
    def resolve():
        n = int(input())
        for _ in range(n):
            Colision.collided()
            
    @staticmethod #-> O(1)
    def collided() -> None:
        dados = [int(x) for x in input().split()]
        XA, YA, XB, YB, XC, YC, XD, YD, RX, RY = dados
        
        print(1 if XA <= RX <= XB and XD <= RX <=
          XC and YA <= RY <= YD and YB <= RY <= YC else 0)
        
Colision.resolve()