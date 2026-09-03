while True:
    try:
        volume = float(input())
        diametro = float(input())
        
        PI = 3.14
        R = diametro / 2
        
        Area = (PI * R**2)
        Altura = volume / Area
        
        print(f"ALTURA = {Altura:.2f}")
        print(f"AREA = {Area:.2f}")
        
    except EOFError:
        break