while True:
    t = int(input())
    if t == 0:
        break

    z = 0
    s = 0
    p = 0
    i = 0

    postes = [int(x) for x in input().split()]

    for n in postes:
        if n == 0 and i == 0:
            z += 1
            p += 1
        elif n == 0 and i == 1:
            p += 1

        if n == 1:
            i = 1
            s += p // 2
            p = 0

    if p > 0:
        s -= z // 2
        p += z
        s += p // 2

    print(s)