class Assembly_Line:
    @staticmethod
    def min_time(e1, e2, x1, x2, line1, line2):
        n = len(line1)
        dp1 = [0] * n
        dp2 = [0] * n

        # Tempo para primeira estação
        dp1[0] = e1 + line1[0][0]
        dp2[0] = e2 + line2[0][0]

        # Para as estações seguintes
        for i in range(1, n):
            # Linha 1: ficar ou trocar vindo da linha 2
            stay1 = dp1[i - 1]
            switch1 = dp2[i - 1] + line2[i - 1][1]  # transição 2->1 do passo anterior
            dp1[i] = line1[i][0] + min(stay1, switch1)

            # Linha 2: ficar ou trocar vindo da linha 1
            stay2 = dp2[i - 1]
            switch2 = dp1[i - 1] + line1[i - 1][1]  # transição 1->2 do passo anterior
            dp2[i] = line2[i][0] + min(stay2, switch2)

        # Soma tempo de saída
        return min(dp1[-1] + x1, dp2[-1] + x2)

    @staticmethod
    def resolve():
        while True:
            try:
                line = input()
                if not line:
                    continue  # pula linhas vazias
                steps = int(line.strip())

                e1, e2 = map(int, input().split())
                line1 = list(map(int, input().split()))
                line2 = list(map(int, input().split()))

                # switch1 e switch2 só existem se steps > 1
                switch1 = list(map(int, input().split())) if steps > 1 else []
                switch2 = list(map(int, input().split())) if steps > 1 else []

                x1, x2 = map(int, input().split())

                # Completa as transições com 0 no final para alinhar com steps
                switch1 += [0] * (steps - len(switch1))
                switch2 += [0] * (steps - len(switch2))

                time1 = [(line1[i], switch1[i]) for i in range(steps)]
                time2 = [(line2[i], switch2[i]) for i in range(steps)]

                print(Assembly_Line.min_time(e1, e2, x1, x2, time1, time2))

            except EOFError:
                break

Assembly_Line.resolve()