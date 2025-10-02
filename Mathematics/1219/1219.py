import math

PI = 3.1415926535897

class Colourful_flowers:
    @staticmethod
    def solve(a: int, b: int, c: int):
        # Semiperímetro e área do triângulo (Heron)
        s = (a + b + c) / 2
        area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
        # Raio do círculo inscrito
        r_in = area_triangle / s
    
        # Raio do círculo circunscrito (c é a hipotenusa)
        R_out = (a * b * c) / (4 * area_triangle)
    
        area_roses = PI * r_in ** 2
        area_violets = area_triangle - area_roses
        area_sunflowers = PI * R_out ** 2 - area_triangle
    
        print(f"{area_sunflowers:.4f} {area_violets:.4f} {area_roses:.4f}")
        
while True:
    try:
        a, b, c = sorted([int(x) for x in input().split()])
        Colourful_flowers.solve(a, b, c)
    except EOFError: break