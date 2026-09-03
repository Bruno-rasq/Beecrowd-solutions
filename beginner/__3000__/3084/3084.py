while True:
    try:
        ah, am = [float(el) for el in input().split()]
        hh = ah // 30
        mm = am // 6

        printf(f"{hh:02}:{mm:02}")

    except EOFError:
        break