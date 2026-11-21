x1, y1, x2, y2, k = [int(x) for x in input().split()]

dist = abs(x2 - x1) + abs(y2 - y1)

if dist <= k: 
    print("SIM") 
else: 
    print("NAO")