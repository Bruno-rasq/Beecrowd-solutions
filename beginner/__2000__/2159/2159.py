import math

n = int(input())
q = n / math.log(n)
PI = 3.14159

limite_minimo = q
limite_maximo = 1.25506 * q

print(f"{limite_minimo:.1f} {limite_maximo:.1f}")