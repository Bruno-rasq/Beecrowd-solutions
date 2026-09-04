local function main()
    local n = tonumber(io.read())
    local gooddeeds = {}
    local uniques = {}

    -- Lê os valores e guarda os únicos
    local values = {}
    for x in io.read():gmatch("%S+") do
        table.insert(values, tonumber(x))
    end
    
    for i = 1, n do
        local gd = values[i]
        gooddeeds[i] = gd
        uniques[gd] = true
    end

    local levels = {}
    for value, _ in pairs(uniques) do
        table.insert(levels, value)
    end

    table.sort(levels)

    -- Cria o mapa: valor -> rank
    local gift = {}
    for rank, value in ipairs(levels) do
        gift[value] = rank
    end

    local ans = 0
    for _, value in ipairs(gooddeeds) do
        ans = ans + gift[value]
    end

    print(ans)
end

main()