while True:
    try:
        modelos_expostos, modelos_danificar = [int(x) for x in input().split()]
        modelos = [int(x) for x in input().split()]
        
        maior_prejuizo = 0
        for i in range(modelos_danificar):
            maior = max(modelos)
            maior_prejuizo += maior
            modelos.remove(maior)
            
        print(maior_prejuizo)
        
    except EOFError:
        break