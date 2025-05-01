while True:
    try:

        n = input()
        cutoff = input()
        
        F = float(n) #converte a entrada para float
        I = int(F)   #converte e pega a parte inteiro do valor
        D = F - I    #calcula a parte decimal do valor
        
        output = I + 1 if D > float(cutoff) else I
        
        print(output)
        
    except EOFError:
        break