def arraylist(n):
    n1 = 0, n2 = n1 - 1

    for i in range(n):
        response = ""
        for j in range(n):
            if (j == n1 and j == n2) or j == n2:
                response += "2"
            elif j == n1:
                response += "1"
            else:
                response += "3"
        print(response)
        n1 += 1
        n2 -= 1

while True:
    try:
        n = int(input())
        arraylist(n)

    except EOFError:
        break