DMPT = 45 # DURACAO_MAXIMA_PRIMEIRO_TEMPO
DMST = 90 # DURACAO_MAXIMA_SEGUNDO_TEMPO

def printOut(tempo, minuto) -> None:
    out = ""
    if tempo == "1T":
        diff = abs(DMPT - minuto)
        out = f"{DMPT}+{diff}" if minuto > DMPT else f"{minuto}"
        
    if tempo == "2T":
        minuto += 45
        diff = abs(DMST - minuto)
        out = f"{DMST}+{diff}" if minuto > DMST else f"{minuto}"
        
    print(out)
        

numero_registros_sumula = int(input())

for _ in range(numero_registros_sumula):
    registro = input().split()
    minuto, tempo = int(registro[0]), registro[1]
    
    printOut(tempo, minuto)