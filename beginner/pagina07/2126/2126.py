c = 1
while True:
    try:
        subseq = input()
        linha = input()
        
        qts = 0
        pos = 0
        
        tamanho_subseq = len(subseq)
        tamanho_linha = len(linha)
        
        for i in range(tamanho_linha - tamanho_subseq + 1):
            eh_sub = True
            for j in range(tamanho_subseq):
                if linha[i + j] != subseq[j]:
                    eh_sub = False
                    break
            if eh_sub:
                qts += 1
                pos = i + 1
                
        print(f"Caso #{c}:")
        if qts == 0:
            print("Nao existe subsequencia")
        else:
            print(f"Qtd.Subsequencias: {qts}")
            print(f"Pos: {pos}")
        print("")
        c += 1
        
    except EOFError:
        break