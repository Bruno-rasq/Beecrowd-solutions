import math

while True:
    try:
        data = [int(x) for x in input().split()]
        DP = 12 #distancia perpendicular - cateto
        DO = data[0] # distancia entre os barcos - cateto
        v1 = data[1] # velocidade barco fugitivo
        v2 = data[2] # velocidade barco guarda_costeira 
        
        # hipotenusa = √(catetoOposto² + catetoAdjacente²)
        distancia_guarda_percorre = math.sqrt(DP**2 + DO**2)
        
        # tempo = espaço / velocidade 
        t1 = 12 / v1
        t2 = distancia_guarda_percorre / v2
        
        print("S" if t2 <= t1 else "N")
        
    except EOFError: break