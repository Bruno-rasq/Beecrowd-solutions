class Sorvete:
    @staticmethod
    def intervalos_na_praia(_, n_sorveteiros):
        intervalos = []
        for _ in range(n_sorveteiros):
            U, V = map(int, input().split())
            intervalos.append((U, V))

        # Ordena por início
        intervalos.sort()

        # Faz o merge dos intervalos
        fundidos = []
        for inicio, fim in intervalos:
            if not fundidos or inicio > fundidos[-1][1]:
                fundidos.append([inicio, fim])
                continue
            
            fundidos[-1][1] = max(fundidos[-1][1], fim)

        # Exibe o resultado
        for i, f in fundidos: print(f"{i} {f}")

teste = 1
while True:
    comprimento, sorveteiros = map(int, input().split())
    if comprimento == sorveteiros == 0:
        break

    print(f"Teste {teste}")
    Sorvete.intervalos_na_praia(comprimento, sorveteiros)
    teste += 1
    print()