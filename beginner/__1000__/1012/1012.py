A, B, C = [float(el) for el in input().split()]

PI = 3.14159

areatringulo = (A * C) / 2.0
circle = PI * (C * C)
trapezium = ((A + B) * C) / 2.0
square = B * B
retangle = A * B

print(f'TRIANGULO: {areatringulo:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {retangle:.3f}')