# delta = b² - 4*a*c
# y == ALTURA MÁXIMA 
# y = -delta / 4*a

n = int(input())
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]

    delta = b**2 - (4*a*c)
    y = -delta / (4 * a)

    print(f"{y:.2f}")