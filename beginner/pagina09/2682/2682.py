


def calcular_angulo_hora(angulo):
    
    # no anhulo  0° já são 6horas (inivio da manha)
    CADA_ANGULO_SEG = 240
    HORA_INICIAL_SEG = 6 * 60 * 60
    
    quantidade_seg_angulo = angulo * CADA_ANGULO_SEG
    total_segundos = HORA_INICIAL_SEG + quantidade_seg_angulo
    
    horas = total_segundos // 3600
    total_segundos = total_segundos - (horas * 3600)
    minutos = total_segundos // 60
    segundos = total_segundos - (minutos * 60)
    
    horas = horas if horas <= 23 else horas - 24
    
    if angulo < 90.0 or angulo == 360.0: print("Bom Dia!!")
    elif angulo < 180.0: print("Boa Tarde!!")
    elif angulo < 270.0: print("Boa Noite!!")
    else: print("De Madrugada!!")
    
    print(
        str(int(horas)).zfill(2), 
        str(int(minutos)).zfill(2), 
        str(int(segundos)).zfill(2), 
        sep=":", end="\n"
    )
    
while True:
    try:
        angulo = float(input())
        calcular_angulo_hora(angulo)
    except EOFError: break