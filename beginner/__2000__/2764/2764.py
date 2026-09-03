while True:
    try:
        dd, mm, yy = input().split('/')
        print(f"{mm}/{dd}/{yy}")
        print(f"{yy}/{mm}/{dd}")
        print(f"{dd}-{mm}-{yy}")

    except EOFError:
        break