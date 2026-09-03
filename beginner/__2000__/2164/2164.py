import math

n = int(input())
R = math.sqrt(5)
fibonacci = ((((1 + R)/2)**n - ((1 - R)/2)**n) / R)

print(f"{fibonacci:.1f}")