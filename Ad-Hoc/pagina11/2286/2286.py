teste = 1

while True:
    n = int(input())

    if n == 0:
        break

    par = input()
    impar = input()

    print(f"teste {teste}")

    for _ in range(n):
        a, b = [int(i) for i in input().split()]
        soma = a + b

        if soma % 2 == 0:
            print(par)
        else:
            print(impar)

    teste += 1
    print('')
