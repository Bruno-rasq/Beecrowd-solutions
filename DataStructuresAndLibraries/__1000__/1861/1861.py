assassinos, mortos = {}, set()

while True:
    try:
        assassino, vitima = input().split()
        mortos.add(vitima)
        
        if assassino not in assassinos:
            assassinos[assassino] = 0
        assassinos[assassino] += 1
        
        if vitima in assassinos:del assassinos[vitima]
        if assassino in mortos: del assassinos[assassino]
    except EOFError: break
   
print("HALL OF MURDERERS")
for assassino in sorted(assassinos):
    print(f"{assassino} {assassinos[assassino]}")