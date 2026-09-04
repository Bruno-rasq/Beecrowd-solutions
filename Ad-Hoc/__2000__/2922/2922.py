while True:
    try:
        n, m = [int(x) for x in input().split()]
        print(max(abs(m - n) - 1, 0))
    except EOFError: break