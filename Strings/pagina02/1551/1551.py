casos_teste = int(input())
for _ in range(casos_teste):
    frase = input()
    
    letras = set()
    
    for char in frase:
        if char.isalpha():
            letras.add(char.lower())
    
    total = len(letras)
    
    if total == 26:
        print("frase completa")
    elif total >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")