arco = 0
escudo = 0
espada = 0
pocao = 0

n = int(input())
for _ in range(n):
    item = input()

    if item == "arco": arco += 1
    if item == "escudo": escudo += 1
    if item == "espada": espada += 1
    if item == "pocao": pocao += 1

print(f"arco {arco}")
print(f"escudo {escudo}")
print(f"espada {espada}")
print(f"pocao {pocao}")