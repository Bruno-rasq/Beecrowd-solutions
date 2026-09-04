
# (BlocoA + i) + (BlocoB + i) = BlocoC
# onde i é o bloco entre BlocoA e BlocoB e seus resultados
# são os Blocos imediatamente abaixo do Bloco C.

def resolver_x(blocoA: int, blocoB: int, blocoC: int) -> int:
    x = (blocoC - (blocoA + blocoB)) / 2
    return int(x)

def addBrickInTheWall(wall: list[list[int]]) -> None:
    _wall = []
    
    for i in range(len(wall) - 1, 0, -1):
        line1, line2 = wall[i], wall[i - 1]
        aux1, aux2 = [], []
    
        for j in range(len(line1) -1):
            blocoA, blocoB = line1[j], line1[j + 1]
            blocoC = line2[j]
            blocoX = resolver_x(blocoA, blocoB, blocoC)
            
            aux1.append(blocoA)
            aux1.append(blocoX)
            aux2.append((blocoA + blocoX))
            aux2.append((blocoB + blocoX))
            
        aux1.append(line1[-1])
        _wall.append(aux1)
        _wall.append(aux2)
    _wall.append(wall[0])
    
    for row in reversed(_wall):
        print(" ".join([str(x) for x in row]))
            
n = int(input())
for _ in range(n):
    wall = [[int(x) for x in input().split()] for _ in range(5)]
    addBrickInTheWall(wall)