import math

TESTE_CASE = 1

while True:
    NUMERO_MEDICOES, INTERVALO_DESEJADO = [int(x) for x in input().split()]

    if NUMERO_MEDICOES == INTERVALO_DESEJADO == 0: break

    MEDICOES = []
    for _ in range(NUMERO_MEDICOES):
        MEDICOES.append(int(input()))

    # Calcula a soma da primeira janela
    soma = sum(MEDICOES[:INTERVALO_DESEJADO])

    MENOR_SOMA_REGISTRADA = soma
    MAIOR_SOMA_REGISTRADA = soma

    # Desliza a janela
    for i in range(INTERVALO_DESEJADO, NUMERO_MEDICOES):
        soma += MEDICOES[i]
        soma -= MEDICOES[i - INTERVALO_DESEJADO]

        MAIOR_SOMA_REGISTRADA = max(MAIOR_SOMA_REGISTRADA, soma)
        MENOR_SOMA_REGISTRADA = min(MENOR_SOMA_REGISTRADA, soma)

    # Como o intervalo é sempre positivo, truncar a média
    # equivale a truncar a soma / intervalo.
    A = math.trunc(MENOR_SOMA_REGISTRADA / INTERVALO_DESEJADO)
    B = math.trunc(MAIOR_SOMA_REGISTRADA / INTERVALO_DESEJADO)

    print(f"Teste {TESTE_CASE}")
    print(f"{A} {B}")
    print()

    TESTE_CASE += 1