def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a, b, c, d = [int(x) for x in input().split()]

num = a * d + c * b
den = b * d

div = mdc(num, den)

num //= div
den //= div

print(num, den)