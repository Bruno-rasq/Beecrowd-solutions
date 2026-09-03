def wordplay(palavra, caso):
    N = len(palavra)
    menor = palavra
    maior = palavra

    for i in range(1, N):
        rotacionada = ""
        for j in range(N):
            rotacionada += palavra[(i + j) % N]

        if rotacionada < menor:
            menor = rotacionada
        if rotacionada > maior:
            maior = rotacionada

    print(f"Caso {caso}: {menor} {maior}")

i = 1 
palavra = input()
while palavra != "*":
    wordplay(palavra, i)
    i += 1
    palavra = input()