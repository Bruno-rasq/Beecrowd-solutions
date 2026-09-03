
casos_teste = int(input())

for _ in range(casos_teste):
    a, b = [int(x) for x in input().split("x")]
    
    m = 5
    
    for i in range(6):
        if a != b:
            print(f"{a} x {m} = {a * m} && {b} x {m} = {b * m}")
        else:
            print(f"{a} x {m} = {a * m}")
            
        m += 1