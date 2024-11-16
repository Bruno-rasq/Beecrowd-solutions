while True:
    try:
        larguraPlaca, alturaPlaca, qntPedidos = map(int, input().split())

        areaPlca = larguraPlaca * alturaPlaca

        for _ in range(qntPedidos):
            larguraPdC, alturaPdc = map(int, input().split())

            areaPlacaPdc = alturaPdc * larguraPdC

            if areaPlacaPdc <= areaPlca and \ 
                ((larguraPdC <= larguraPlaca) and (alturaPdc <= alturaPlaca) or 
                (larguraPdC <= alturaPlaca and alturaPdc <= larguraPlaca)):
                print("Sim")
            else:
                print("Nao")

    except EOFError:
        break 