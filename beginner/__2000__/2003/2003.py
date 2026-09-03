while True:
    try:
        hora, minuto = [int(x) for x in input().split(":")]
        
        tempo_chegar_ponto = 60
        
        horario_encontro_em_minutos = 480 #8 * 60
        
        tempo_em_minutos_ponto = (hora * 60) + minuto + tempo_chegar_ponto
        
        atraso = 0
        if tempo_em_minutos_ponto <= horario_encontro_em_minutos:
            print(f"Atraso maximo: {atraso}")
        else:
            
            atraso = tempo_em_minutos_ponto - horario_encontro_em_minutos
            print(f"Atraso maximo: {atraso}")
    except EOFError:
        break