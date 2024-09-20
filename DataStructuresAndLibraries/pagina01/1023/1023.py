import math

t = 0
while True:
    try:
        n = int(input())

        if n == 0:
            break

        totalx, totaly = 0, 0
        consumos = []

        for _ in range(n):
            x, y = [int(el) for el in input().split(" ")]

            totalx += x
            totaly += y

            if y // x in consumos:
                consumos[y//x] += x
            else:
                consumos[y//x] = x


        consumo_total = ((100 * totaly) / totalx) / 100

        t += 1
        print(f"Cidade# {t}:")

        output = []
        keys = sorted(list(consumos.key()))
        for key in keys:
            output.append(f"{consumos[key]}-{key}")

        print(f"{" ".join(output)}")

        consumo_medio = math.floor(consumo_total)

        print(f"Consumo medio: {consumo_medio:.2f} m3.")


    except EOFError:
        break