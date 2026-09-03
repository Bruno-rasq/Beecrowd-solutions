import sys

for linha in sys.stdin:
    try:
        angulo = int(linha.strip())

        if 0 <= angulo < 90 or angulo == 360:
            print("Bom Dia!!")
        elif 90 <= angulo < 180:
            print("Boa Tarde!!")
        elif 180 <= angulo < 270:
            print("Boa Noite!!")
        elif 270 <= angulo < 360:
            print("De Madrugada!!")
    except:
        continue