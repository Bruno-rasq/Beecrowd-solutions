while True:
    try:
        line = input()
        tag_i = False
        tag_b = False

        response = ""
        for char in line:

            if char == "*" and not tag_b:
                response += "<b>"
                tag_b = True

            elif tag_b and char == "*":
                response += "</b>"
                tag_b = False

            elif char == "_" and not tag_i:
                response += "<i>"
                tag_b = True

            elif tag_i and char == "_":
                response += "</i>"
                tag_b = False

            else:
                response += char
        
        print(response)
    except EOFError:
        break