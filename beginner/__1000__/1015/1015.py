import math

x1, y1 = [float(num) for num in input().split()]
x2, y2 = [float(num) for num in input().split()]

distance = math.sqrt(
    pow((x2 - x1), 2) + pow((y2 - y1), 2)
)

print(f"{distance:.4f}")