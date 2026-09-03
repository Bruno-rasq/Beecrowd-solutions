while True:
    try:
        m = int(input())
        
        numerador = 0
        denominador = 0
        
        for i in range(m):
            n, c = [int(x) for x in input().split()]
            
            numerador += n * c
            denominador += c * 100
            
        resultado = numerador / denominador
        print(f"{resultado:.4f}")
    except EOFError:
        break