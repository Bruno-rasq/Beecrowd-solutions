
casos_teste = int(input())

for _ in range(casos_teste):
    RA = input()
    if not RA.startswith("RA") or len(RA) != 20:
        print("INVALID DATA")
        
    RA = RA[1:] #remove o primeiro caracter
    RA = RA[1:] #remove o primeiro caracter
    i = 0
    while RA[i] == "0":
        RA = RA[1:]
            
    print(RA)