tabela_preprocessada = [
    4, 9, 25, 81, 289, 1089, 4225, 16641, 66049, 263169,
    1050625, 4198401, 16785409, 67125249, 268468225,
    1073807361
]

i = 1
while True:
    n = int(input())
    if n == -1: break 
    print(f"Teste {i}")
    print(tabela_preprocessada[n])
    print()
    i += 1