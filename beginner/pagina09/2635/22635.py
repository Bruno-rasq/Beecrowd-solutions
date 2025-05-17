
while True:
    try:
        n_palavras = int(input())
        HISTORICO = [input() for _ in range(n_palavras)]
        
        n_pesquisas = int(input())
        for _ in range(n_pesquisas):
            pesquisa = input()
            
            sugestoes = []
            maior_palavra = 0
            
            for palavra in HISTORICO:
                if palavra.startswith(pesquisa):
                    sugestoes.append(palavra)
                    if len(palavra) > maior_palavra:
                        maior_palavra = len(palavra)
                        
            print("-1" if len(sugestoes) == 0 else f"{len(sugestoes)} {maior_palavra}")
            
    except EOFError: break