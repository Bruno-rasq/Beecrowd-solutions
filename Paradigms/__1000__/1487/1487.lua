local instancia = 1
while true do

    local n, capacity = io.read("*n", "*n")
    if n == 0 and capacity == 0 then break end

    -- LÊ OS DADOS DE ENTRADA.
    local itens = {}
    for i = 1, n do
        itens[i] = {io.read("*n", "*n")}
    end

    -- INICIA TABELA COM PREENCHIMENTO EM ZERO.
    -- dp[w] = maior valor possível usando capacidade w.
    local dp = {}
    for w = 0, capacity do
        dp[w] = 0
    end

    -- KNAPSACK
    for w = 1, capacity do
        for idx, data in ipairs(itens) do
            local peso = data[1]
            local valor = data[2]
            if peso <= w then
                dp[w] = math.max(dp[w], dp[w - peso] + valor)
            end
        end
    end

    print(string.format("Instancia %d", instancia))
    print(dp[capacity])
    print()
    instancia = instancia + 1
end