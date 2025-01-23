import math

while True:

    try:

        r1, x1, y1, r2, x2, y2 = [int(n) for n in input().split()]
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if distancia + r2 < r1:
            print("RICO")
        else:
            print("MORTO")

    except EOFError:
        break