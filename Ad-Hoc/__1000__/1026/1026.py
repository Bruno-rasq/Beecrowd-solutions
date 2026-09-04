while True:
    try:
        a, b = [int(x) for x in input().split()]
        c = a ^ b
        print(c)
    except: break