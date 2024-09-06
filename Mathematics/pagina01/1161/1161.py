def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


while True:
    try:
        a, b = [int(el) for el in input().split()]

        fatorialA = fatorial(a)
        fatorialB = fatorial(b)

        print(fatorialA + fatorialB)
    except EOFError:
        break;