cs_teste = int(input())

for _ in range(cs_teste):
    A, B = input().split()

    if len(B) > len(A):
        print("nao encaixa")
        continue

    pertence = True
    for i in range(1, len(B)+1):
        if A[-i] != B[-i]:
            pertence = False
            break

    print("encaixa" if pertence else "nao encaixa")