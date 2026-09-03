A = input()
B = input()

i = 0
while True:
    # Se chegamos ao fim de uma das strings
    if i >= len(A) or i >= len(B):
        if len(A) < len(B):
            print(A)
            print(B)
        else:
            print(B)
            print(A)
        break

    a = ord(A[i])
    b = ord(B[i])

    if a < b:
        print(A)
        print(B)
        break
    elif b < a:
        print(B)
        print(A)
        break
    else:
        i += 1