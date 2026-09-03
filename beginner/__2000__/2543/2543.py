while True:
    try:
        videos_publicado, meu_ID = [int(x) for x in input().split()]
        
        contador = 0
        for _ in range(videos_publicado):
            ID, categoria = [int(x) for x in input().split()]
            
            if ID == meu_ID and categoria == 0:
                contador += 1
                
        print(contador)
    except EOFError:
        break