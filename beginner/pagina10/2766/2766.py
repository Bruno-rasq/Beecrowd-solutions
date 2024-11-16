index = 1
while True:
    try:
        entrada = input()
        if index == 3 or index == 7 or index == 9:
            print(entrada)
        index += 1
    except EOFError:
        break