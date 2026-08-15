-- Variações de casas que o dado cavalo consegue chegar.
local DELTA = {
    {2, 1}, {1, 2},
    {-1, 2}, {-2, 1},
    {-2, -1}, {-1, -2},
    {1, -2}, {2, -1}
}

local source, target = io.read():match("(%S+) (%S+)")

local function possiblePlay(source, target)
    -- Coordenada do cavalo.
    local sx = string.byte(source, 1) - string.byte("a") + 1
    local sy = tonumber(source:sub(2, 2))

    -- Coordenada de destino.
    local tx = string.byte(target, 1) - string.byte("a") + 1
    local ty = tonumber(target:sub(2, 2))

    for _, delta in ipairs(DELTA) do
        local nx = sx + delta[1]
        local ny = sy + delta[2]
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8 then
            if nx == tx and ny == ty then
                return true
            end
        end
    end
    return false
end

if possiblePlay(source, target) then
    print("VALIDO")
else
    print("INVALIDO")
end