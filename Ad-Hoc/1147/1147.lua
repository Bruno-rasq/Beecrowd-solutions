-- coordenadas das cadas adjacentes que o cavalo pode alcançar 
local KNIGHTDELTA = {
    {-2, -1}, {-2,  1},     -- cima esquerda e cima direita
    {-1,  2}, {1,   2},     -- direita cima e direita baixo
    {2,  -1}, {2,   1},     -- baixo esquerda e baixo direita
    {-1, -2}, {1,  -2}      -- esquerda cima e esquerda baixo
}

-- coordenada as casas adjacentes que o peão pode alcança.
local PAWNDELTA = {
    {1, -1},                 -- diagonal esquerda
    {1,  1}                  -- diagonal direita
}

local function knightScape(knightPosition, iteration)
    local dangerousPos = {}
    
    -- lê as coordenadas dos 8 peões 
    for i=1, 8 do
        local pawnpos = io.read()
        local row = 9 - tonumber(string.sub(pawnpos, 1, 1))
        local col = string.byte(pawnpos, 2, 2) - 96 

        for i=1, #PAWNDELTA do 
            local nx = row + PAWNDELTA[i][1]
            local ny = col + PAWNDELTA[i][2]
            if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8 then
                table.insert(dangerousPos, string.format("%d %d", nx, ny))
            end
        end
    end

    local ans = 0
    local KR = 9 - tonumber(string.sub(knightPosition, 1, 1))
    local KC = string.byte(knightPosition, 2, 2) - 96
    for i=1, #KNIGHTDELTA do
        local nx = KR + KNIGHTDELTA[i][1]
        local ny = KC + KNIGHTDELTA[i][2]
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8 then
            local pos = string.format("%d %d", nx, ny)
            local safePos = true
            for i=1, #dangerousPos do
                if pos == dangerousPos[i] then 
                    safePos = false
                    break
                end
            end
            if safePos then ans = ans + 1 end
        end
    end

    print(string.format("Caso de Teste #%d: %d movimento(s).", iteration, ans))
end

local function main()
    local i = 1
    while true do
        local knightPosition = io.read()
        if knightPosition == "0" then break end

        knightScape(knightPosition, i)
        i = i + 1
    end
end

main() 