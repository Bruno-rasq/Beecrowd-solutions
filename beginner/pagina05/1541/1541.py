import math

while True:
    data = input()
    if data == "0":
        break
    
    Base, Altura, porcent = [int(x) for x in data.split()]
    
    area_casa = Base * Altura
    area_terreno = area_casa / (porcent / 100)
    lado = math.trunc(math.sqrt(area_terreno))
    
    print(lado)