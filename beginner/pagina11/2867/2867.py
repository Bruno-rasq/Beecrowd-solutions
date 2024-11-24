casos = int(input())

for _ in range(casos):
    a, b = [int(n) for n in input().split()]
    pot = a ** b
    num_digits = lent(str(pot))

    print(num_digits)