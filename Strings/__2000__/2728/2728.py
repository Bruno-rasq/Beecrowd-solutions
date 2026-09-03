while True:
    try:
        entrada = input().strip()
        palavras = entrada.split("-")
        
        cobol = "cobol"
        valido = True
        
        for i in range(5):
            letra = cobol[i]
            palavra = palavras[i].lower()
            
            # Verifica se a letra está no início ou fim da palavra
            if not (palavra.startswith(letra) or palavra.endswith(letra)):
                valido = False
                break
        
        print("GRACE HOPPER" if valido else "BUG")
        
    except EOFError:
        break