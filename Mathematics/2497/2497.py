exp = 0
while True:
    estapas = int(input())
    if estapas == -1: break
    ciclos = estapas // 2
    exp += 1
    
    print(f"Experiment {exp}: {ciclos} full cycle(s)")