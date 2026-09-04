while (rodadas := int(input())) != 0:
    
    bonus_recebido = False
    
    #bonus -> elemento atual, contador
    pontos_m, pontos_l, bonus_m, bonus_l = 0, 0, (0, 0), (0, 0)

    mark_bakugans = [int(x) for x in input().split()]
    leti_bakugans = [int(x) for x in input().split()]
    
    for i in range(rodadas):
        pontos_m += mark_bakugans[i]
        pontos_l += leti_bakugans[i]
        
        bonus_m = (bonus_m[0], bonus_m[1] + 1) if bonus_m[0] == mark_bakugans[i] else (mark_bakugans[i], 0)
        bonus_l = (bonus_l[0], bonus_l[1] + 1) if bonus_l[0] == leti_bakugans[i] else (leti_bakugans[i], 0)
        
        if not bonus_recebido:
            if bonus_m[1] == 2 and bonus_l[1] == 2:
                bonus_recebido = True
    
            elif bonus_m[1] == 2 and bonus_l[1] != 2:
                pontos_m += 30
                bonus_recebido = True
                
            elif bonus_l[1] == 2 and bonus_m[1] != 2:
                pontos_l += 30
                bonus_recebido = True

    if pontos_m == pontos_l: print("T")
    else: print("M" if pontos_m > pontos_l else "L")