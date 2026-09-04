caso_teste = 1
while num_dicks := int(input()):
    
    if num_dicks == 0: break
        
    moves = (2 ** num_dicks) - 1
    print(f"Teste {caso_teste}")
    print(f"{moves}")
    print()
    caso_teste += 1
