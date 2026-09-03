arvores = int(input())

for _ in range(arvores):
    h, e, g = [int(x) for x in input().split()]
    
    requisito = (h >= 200 and h <= 300)and (e >= 50) and (g >= 150)
    print("Sim" if requisito else "Nao")