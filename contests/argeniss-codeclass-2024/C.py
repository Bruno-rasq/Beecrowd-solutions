while True:
    try:
        alfabet = input()
        length = int(input())
        keys = [int(key) for key in input().split()]

        resp = ""
        for i in range(length):
            key = keys[i] - 1
            resp += alfabet[key]

        print(resp)

    except EOFError:
        break