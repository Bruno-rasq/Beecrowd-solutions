n = int(input())

while n > 0:
    posicaoAtual = 2
    contador = 0

    for _ in range(n):

        linha = input().strip()

        if linha == "0 1 1" and posicaoAtual != 1:
            contador += abs(posicaoAtual - 1)
            posicaoAtual = 1

        elif linha == "1 0 1" and posicaoAtual != 2:
            contador += abs(posicaoAtual - 2)
            posicaoAtual = 2
        
        elif linha == "1 1 0" and posicaoAtual != 3:
            contador += abs(posicaoAtual - 3)
            posicaoAtual = 3

    print(contador)
    n = int(input())
