tag = False
while True:
    try:
        line = input()
        if "<body>" in line:
            tag = True
            continue

        elif "</body>" in line:
            break

        if tag:
            print(line)

    except EOFError:
        break