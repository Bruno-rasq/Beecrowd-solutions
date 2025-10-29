caso_teste = 1
while True:
    n = int(input())
    if n == 0:
        break

    pontos_aldo = 0
    pontos_beto = 0

    for _ in range(n):
        a, b = map(int, input().split())
        pontos_aldo += a
        pontos_beto += b

    print(f"Teste {caso_teste}")
    if pontos_aldo > pontos_beto:
        print("Aldo")
    else:
        print("Beto")
    print()  # Linha em branco entre os casos de teste

    caso_teste += 1
