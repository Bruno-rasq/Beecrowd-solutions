a, b = [float(n) for n in input().split()]

if a == 0 and b == 0:
    print("Origem")
elif  a == 0:
    print("Eixo Y")
elif  b == 0:
    print("Eixo X")
elif  b > 0 and a > 0:
    print("Q1")
elif  b > 0 and a < 0:
    print("Q2")
elif  b < 0 and a < 0:
    print("Q3")
elif  b < 0 and a > 0:
    print("Q4")