totalLanches, lanchesPorPessoa, pessoasJaServidas = [int(x) for x in input().split()]

if (totalLanches - (lanchesPorPessoa * pessoasJaServidas)) >= lanchesPorPessoa:
    print("SIM")
else:
    print("NAO")