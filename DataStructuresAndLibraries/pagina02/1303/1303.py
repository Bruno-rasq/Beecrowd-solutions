from collections import defaultdict

class Spurs_Rocks:

    @staticmethod
    def resolve():
        i = 1  # Corrigido: precisa estar fora do loop
        while True:
            n = int(input())
            if n == 0:
                break
            if i > 1:
                print()

            ranking = Spurs_Rocks.set_times(n)

            instancia = []
            # Percorrer ordenado como no C++
            for pontos in sorted(ranking, reverse=True):
                for media in sorted(ranking[pontos], reverse=True):
                    for marcados in sorted(ranking[pontos][media], reverse=True):
                        for time in sorted(ranking[pontos][media][marcados]):
                            instancia.append(str(time))

            print(f"Instancia {i}")
            print(" ".join(instancia))
            i += 1

    @staticmethod
    def set_times(n: int):
        # times[time] = [marcados, recebidos, pontos]
        times = defaultdict(lambda: [0, 0, 0])
        for _ in range(n * (n - 1) // 2):
            TA, PA, TB, PB = map(int, input().split())

            times[TA][0] += PA
            times[TA][1] += PB
            times[TA][2] += 2 if PA > PB else 1

            times[TB][0] += PB
            times[TB][1] += PA
            times[TB][2] += 2 if PB > PA else 1

        ranking = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
        for time in times:
            marcados, recebidos, pontos = times[time]
            # Corrigido: usar média real (float), como no código C++
            media = marcados / recebidos if recebidos != 0 else float(marcados)
            # Para garantir ordenação correta, armazenar a média com várias casas decimais (ou usar round)
            ranking[pontos][media][marcados].append(time)

        return ranking

# Execução
Spurs_Rocks.resolve()