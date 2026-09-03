a, b = [float(el) for el in input().split()]


result = (
    ((1.0 + a / 100) * (1.0 + b / 100)) - 1.0
) * 100

print(f"{result:.6f}")