while True:
    try:
        alien_vowels = input()
        frase = input().split()
        count = 0
        
        for palavra in frase:
            for char in palavra:
                if char in alien_vowels:
                    count += 1
                    
        print(count)
    except EOFError:
        break