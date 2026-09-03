while True:
    try:
        total_char, max_linhas, max_chars = [int(x) for x in input().split()]
        conto = input().split()
        
        qnt_paginas = 0
        i = 0
        
        while i < len(conto):
            linhas = 0  # contador de linhas da página atual
            while linhas < max_linhas and i < len(conto):
                # tenta montar uma linha
                linha_len = 0
                while i < len(conto):
                    palavra = conto[i]
                    if linha_len == 0:
                        if len(palavra) <= max_chars:
                            linha_len = len(palavra)
                            i += 1
                        else:
                            break  # palavra grande demais
                    elif linha_len + 1 + len(palavra) <= max_chars:
                        linha_len += 1 + len(palavra)  # +1 pelo espaço
                        i += 1
                    else:
                        break  # não cabe mais na linha
                linhas += 1
            qnt_paginas += 1  # terminou uma página
        
        print(qnt_paginas)
    except EOFError:
        break