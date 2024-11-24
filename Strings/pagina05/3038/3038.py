while True:
    try:
        line = input()
        decrypt = ""

        for char in line:
            if char == "@":
                decrypt += 'a'
            elif char == "&":
                decrypt += 'e'
            elif char == "!":
                decrypt += 'i'
            elif char == "*":
                decrypt += 'o'
            elif char == "#":
                decrypt += 'u'
            else:
                decrypt += char

        print(decrypt)
    except EOFError:
        break
