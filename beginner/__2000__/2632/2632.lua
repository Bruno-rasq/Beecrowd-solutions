SPELLS = {
    ["fire"]  = {damage= 200, level= {20, 30, 50}},
    ["water"] = {damage= 300, level= {10, 25, 40}},
    ["earth"] = {damage= 400, level= {25, 55, 70}},
    ["air"]   = {damage= 100, level= {18, 38, 60}}
}

-- Lê a quantidade de casos de teste e limpa a quebra de linha
local t = tonumber(io.read("*l"))
for i=1, t do
    
    -- 1. Lê a linha INTEIRA do caso de teste de uma vez só
    local enemyline = io.read("*l"):gmatch("%S+")
    local playerline = io.read("*l"):gmatch("%S+")
    
    -- 2. Extrai os atributos usando o devido iterador!
    local width  = tonumber(enemyline())
    local height = tonumber(enemyline())
    local x0     = tonumber(enemyline())
    local y0     = tonumber(enemyline())
    local typeSpell = playerline()
    local level     = tonumber(playerline())
    local cx        = tonumber(playerline())
    local cy        = tonumber(playerline())

    -- Busca as propriedades da magia na tabela
    local damage = SPELLS[typeSpell].damage
    local radius = SPELLS[typeSpell].level[level]

    -- Calcular os limites do retângulo
    local left = x0
    local right = x0 + width
    local bottom = y0
    local top = y0 + height

    -- Determinar a interseção entre o círculo e o retângulo
    local closestX = math.max(left, math.min(cx, right))
    local closestY = math.max(bottom, math.min(cy, top))

    local distanceSquared = ((closestX - cx) * (closestX - cx)) + 
                            ((closestY - cy) * (closestY - cy))

    if distanceSquared > (radius * radius) then damage = 0  end 

    print(damage)
end