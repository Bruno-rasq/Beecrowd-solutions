import math

n = int(input())
for _ in range(n):
    volume_max, width = [int(x) for x in input().split()]
    F, J = [0,0], [0, 0]
    
    for x in range(width):
        line = input()
        for y, char in enumerate(line):
            if char == 'F': F = [x, y]
            if char == 'J': J = [x, y]
          
    dist = int(math.sqrt((J[0] - F[0])**2 + (J[1] - F[1])**2) * 10)
    vol = math.floor(volume_max / 0.99**dist)
            
    print(f"{vol} dBs")