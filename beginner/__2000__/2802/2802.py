n = int(input())
segmentos = 1 + (((n - 1) * n) / 2) + ((n * (n - 1) * (n - 2) * (n - 3)) / 24)

print(f"{segmentos:.0f}")