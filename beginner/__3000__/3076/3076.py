while True:
    try:
        data = int(input())

        if data <= 100:
            print(1)
        else:

            seculo = data // 100
            if data % 100 != 0:
                seculo += 1
            print(seculo)

    except EOFError:
        break