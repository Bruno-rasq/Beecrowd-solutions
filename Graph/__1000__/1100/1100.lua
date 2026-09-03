-- coordenadas das cadas adjacentes que o cavalo pode alcançar 
local KNIGHTDELTA = {
    {-2, -1}, {-2,  1},     -- cima esquerda e cima direita
    {-1,  2}, {1,   2},     -- direita cima e direita baixo
    {2,  -1}, {2,   1},     -- baixo esquerda e baixo direita
    {-1, -2}, {1,  -2}      -- esquerda cima e esquerda baixo
}

local function BFS(source, target)
    if source == target then return 0 end 
    local sx = 9 - tonumber(string.sub(source, 2, 2))    -- coordenada inicial x.
    local sy = string.byte(source, 1, 1) - 96            -- coordenada inicial y.
    local tx = 9 - tonumber(string.sub(target, 2, 2))    -- coordenada final x.
    local ty = string.byte(target, 1, 1) - 96            -- coordenada final y.
    local queue = {}                                     -- fila de possíveis jogadas.
    local visited = {}                                   -- posições já visitadas.
    local head = 1                                       -- idx da jogada na fila.

    table.insert(queue, {x = sx, y = sy, moves = 0})
    visited[string.format("%d%d", sx, sy)] = true
    
    while head <= #queue do
        local curr = queue[head]
        head = head + 1
        for i=1, #KNIGHTDELTA do
            local nx = curr.x + KNIGHTDELTA[i][1]
            local ny = curr.y + KNIGHTDELTA[i][2]
            if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8 then
                if nx == tx and ny == ty then return curr.moves + 1 end 
                local nextpos = string.format("%d%d", nx, ny)
                if not visited[nextpos] then
                    visited[nextpos] = true
                    table.insert(queue, {
                            x = nx,
                            y = ny,
                            moves = curr.moves + 1
                    })
                end
            end
        end
    end
    return -1
end

local function main()
    while true do
        local line = io.read()
        if not line then break end

        local source, target = line:match("(%S+) (%S+)")
        local moves = BFS(source, target)

        print(string.format(
                "To get from %s to %s takes %d knight moves.",
                source, target, moves))
    end 
end

main() 