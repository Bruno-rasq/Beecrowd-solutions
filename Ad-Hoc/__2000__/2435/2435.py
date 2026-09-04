def Tempo(distancie, velocidade):
    return distancie / velocidade

class Corrida:
    @staticmethod
    def solve(charreteA, charreteB) -> None:
        TA = Tempo(charreteA[1], charreteA[2])
        TB = Tempo(charreteB[1], charreteB[2])
        
        if TA < TB:
            print(charreteA[0])
            return
        
        print(charreteB[0])
        
charreteA = [int(x) for x in input().split()]
charreteB = [int(x) for x in input().split()]

Corrida.solve(charreteA, charreteB)