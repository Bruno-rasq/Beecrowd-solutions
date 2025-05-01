import math

while True:
    try:
        horas, minutos = [int(x) for x in input().split()]
        valores_mensurados = [float(x) for x in input().split()]
        
        QT = int(horas * 60 / minutos) #numero de testes feitos
        X = sum(valores_mensurados) / len(valores_mensurados)
        
        sigma = sum([(valor - X)**2 for valor in valores_mensurados])
        precisao = 0.0
        
        precisao += math.sqrt(
            sigma / (QT-1)
        )
        
        print(f"{precisao:.5f}")
        
    except EOFError:
        break