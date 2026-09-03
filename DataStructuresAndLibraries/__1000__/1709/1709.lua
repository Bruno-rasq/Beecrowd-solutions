-- Calcula a nova posição que a carta terá após um embaralhamento.
local function new_position(pos, n)
    local mid = math.ceil(n / 2)
    if pos < mid then return pos * 2 + 1 end
    return (pos - mid) * 2
end

local n = tonumber(io.read())
local pos = 1
local steps = 1

local aux = new_position(pos, n)
while aux ~= pos do
    steps = steps + 1
    aux = new_position(aux, n)
end

print(steps)