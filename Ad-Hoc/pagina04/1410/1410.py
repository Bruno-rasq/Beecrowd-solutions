while (INPUT := [int(x) for x in input().split()]) and INPUT[0] + INPUT[1]:

    atacantes = [int(x) for x in input().split()]
    defensores = sorted([int(x) for x in input().split()])
    
    atacantes_mais_proximo_gol = min(atacantes)
    penultimo_defensor = defensores[1]
    
    print("Y" if atacantes_mais_proximo_gol < penultimo_defensor else "N")
    