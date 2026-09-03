n = int(input())
vogais = ['a', 'e', 'i', 'o', 'u']

for _ in range(n):
    sobrenome = input()
    aux = sobrenome.lower()
    hard = False
    count = 0

    for char in aux:
        if char not in vogais:
            count += 1
        else:
            count = 0

        if count == 3:
            hard = True
            break

    if hard:
        print(f"{sobrenome} nao eh facil")
    else:
       print(f"{sobrenome} eh facil") 