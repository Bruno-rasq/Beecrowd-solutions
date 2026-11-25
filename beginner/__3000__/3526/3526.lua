local totalLanches, lancherPorPessoa, pessoasServidas = io.read("*n", "*n", "*n")

if (totalLanches - (lancherPorPessoa * pessoasServidas)) >= lancherPorPessoa then
    print("SIM")
else
    print("NAO")
end