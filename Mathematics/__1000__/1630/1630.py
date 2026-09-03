def gdc(a, b):
    if b == 0: return a
    return gdc(b, a % b)

while True:
    try:
        x, y = [int(x) for x in input().split()]
        if x == y:
            print(4)
            continue
        
        stakes = (2*(x + y)) / gdc(x,y)
        print(int(stakes))
    except: break