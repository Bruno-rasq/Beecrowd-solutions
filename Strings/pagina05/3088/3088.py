def fiexText(text):
    fixed = ""
    for i in range(len(text)):
        char = text[i]
        if i < len(text) - 1:
            next = text[i + 1]
            if char == " " and (next == "," or next == "."):
                continue
        fixed += char
    return fixed

while True:
    try:
        line = input()
        print(fiexText(line))
    except EOFError:
        break
