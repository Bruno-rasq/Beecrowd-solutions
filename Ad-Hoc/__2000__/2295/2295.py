class Frota_de_Taxi:
    @staticmethod
    def solve(A: float, G: float, Ra: float, Rg: float) -> None:
        coeA = (Ra / A) 
        coeG = (Rg / G)
        print("G" if coeG >= coeA else "A")
        

a, r, ra, rg = [float(x) for x in input().split()]
Frota_de_Taxi.solve(a, r, ra, rg)