while True:
    try:
        bateria = int(input())
        velocidades = []
        
        for i in range(bateria):
            velocidades.append(float(input()))
            
        print(min(velocidades))
    except EOFError:
        break