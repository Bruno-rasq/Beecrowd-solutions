n = int(input())

for i in range(n):
    a = i + 1
    b = a * a
    c = a * a * a

    print(f"{a} {b} {c}")
    print(f"{a} {b + 1} {c + 1}")