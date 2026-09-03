local function Binary_Search(names)
    local N = #names
    local LEFT = 1
    local RIGHT = N

    while LEFT <= RIGHT do
        local MID = (LEFT + RIGHT) // 2

        local forceA = 0
        local forceB = 0

        -- Calcula a força do grupo A.
        for idx = 1, MID do
            forceA = forceA + names[idx][2] * (MID - idx + 1)
        end

        -- Calcula a força do grupo B.
        for idx = MID + 1, N do
            forceB = forceB + names[idx][2] * (idx - MID)
        end

        -- Achou o aluno pivo que faz com que os dois times tenham a mesma
        -- força.
        if forceA == forceB then
            return names[MID][1]
        end

        if forceA > forceB then
            RIGHT = MID - 1
        else
            LEFT = MID + 1
        end
    end

    return "Impossibilidade de empate."
end

while true do
    local n = tonumber(io.read())
    if n == 0 then break end

    -- Lê os nomes e atribui uma força base somando o valor ASCII de cada
    -- caracter que constitui o nome.
    local names = {}
    for i = 1, n do
        local name = io.read()
        local force = 0
        for charidx = 1, #name do
            force = force + string.byte(name, charidx)
        end

        names[#names + 1] = {name, force}
    end

    print(Binary_Search(names))
end