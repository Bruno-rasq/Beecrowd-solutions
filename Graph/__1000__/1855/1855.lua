local DIRECTIONS = {
    [">"] = {0, 1},
    ["^"] = {-1, 0},
    ["v"] = {1, 0},
    ["<"] = {0, -1}
}

local COL = tonumber(io.read())
local ROW = tonumber(io.read())

local map = {}

for i = 1, ROW do
    local line = io.read()
    local row = {}

    for j = 1, COL do
        row[j] = line:sub(j, j)
    end

    map[i] = row
end

local x = 1
local y = 1

-- DIREÇÃO INICIAL
local direction = DIRECTIONS[map[x][y]]
local dx = direction[1]
local dy = direction[2]

local visiteds = {}

local ans = "!"

repeat

    -- CHEGOU AO BAÚ
    if map[x][y] == "*" then
        ans = "*"
        break
    end

    -- ESTADO ATUAL
    local state = x .. "-" .. y .. "-" .. dx .. "-" .. dy

    -- ENTROU EM LOOP
    if visiteds[state] then
        break
    end

    visiteds[state] = true

    -- SE ENCONTROU UMA SETA, MUDA A DIREÇÃO
    local new_direction = DIRECTIONS[map[x][y]]

    if new_direction then
        dx = new_direction[1]
        dy = new_direction[2]
    end

    -- AVANÇA
    x = x + dx
    y = y + dy

until x < 1 or x > ROW or y < 1 or y > COL

print(ans)