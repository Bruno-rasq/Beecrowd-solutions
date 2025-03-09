import math
while True:
    tempo_seg = int(input())
    if tempo_seg == 0:
        break
    
    Alemanha_gols = math.ceil(7* tempo_seg / 90)
    Brasil_gols = math.floor(tempo_seg / 90)
    
    print(f"Brasil {Brasil_gols} x Alemanha {Alemanha_gols}")