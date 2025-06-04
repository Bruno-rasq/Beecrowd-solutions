while True:
    try:
        qnt_sapatos = int(input())
        
        colecoes_sapatos = {}
        
        for _ in range(qnt_sapatos):
            tamanho, pe = input().split()
            if tamanho not in colecoes_sapatos:
                colecoes_sapatos[tamanho] = (0, 0)
            
            esq, dir = colecoes_sapatos[tamanho]
            if pe == "E":
                esq += 1
            else:
                dir += 1
            colecoes_sapatos[tamanho] = (esq, dir)
        
        total_pares = 0
        for qnt_esq, qnt_dir in colecoes_sapatos.values():
            total_pares += min(qnt_esq, qnt_dir)
        
        print(total_pares)
        
    except EOFError:
        break