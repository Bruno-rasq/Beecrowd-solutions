-- MACROS
local ALLCOLLECTEDGEMS = 31
local DELTAS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
local GEMS = {["p"] = 4, ["t"] = 3, ["m"] = 2, ["e"] = 1, ["r"] = 0}

local function SET(collection, idx)
    return collection | (1 << idx)
end

local function QUERY(collection, idx)
    return (collection & (1 << idx)) ~= 0
end

local function Stringfy(x, y, keys, gems)
    return string.format("%d-%d-%d-%d", x, y, keys, gems)
end

local function FINDKEY(keys, cell)
    if cell == "a" then return SET(keys, 3) end
    if cell == "b" then return SET(keys, 2) end
    if cell == "c" then return SET(keys, 1) end
    if cell == "d" then return SET(keys, 0) end
    return keys
end

local function FINDGEM(gems, cell)
    local idx = GEMS[cell]
    if idx ~= nil then
        return SET(gems, idx)
    end
    return gems
end

local function BFS(board, n, m, x, y)
    local head = 1
    local queue = {}
    local visited = {}

    queue[1] = {X = x, Y = y, keys = 0, gems = 0, steps = 0}
    visited[Stringfy(x, y, 0, 0)] = true

    while head <= #queue do
        local curr = queue[head]
        head = head + 1

        if curr.gems == ALLCOLLECTEDGEMS then
            return curr.steps
        end

        for i = 1, 4 do
            local nx = curr.X + DELTAS[i][1]
            local ny = curr.Y + DELTAS[i][2]

            if nx <= 0 or nx > n or ny <= 0 or ny > m then
                goto continue
            end

            local cell = board[nx]:sub(ny, ny)

            if cell == "#" then goto continue end

            if cell == "A" and not QUERY(curr.keys, 3) then goto continue end
            if cell == "B" and not QUERY(curr.keys, 2) then goto continue end
            if cell == "C" and not QUERY(curr.keys, 1) then goto continue end
            if cell == "D" and not QUERY(curr.keys, 0) then goto continue end

            local nextKeys = FINDKEY(curr.keys, cell)
            local nextGems = FINDGEM(curr.gems, cell)
            local state = Stringfy(nx, ny, nextKeys, nextGems)

            if not visited[state] then
                visited[state] = true
                queue[#queue + 1] = {
                    X = nx,
                    Y = ny,
                    keys = nextKeys,
                    gems = nextGems,
                    steps = curr.steps + 1
                }
            end

            ::continue::
        end
    end

    return -1
end

local function main()
    local n, m = io.read("*n", "*n")
    io.read("*l") -- consome o '\n' restante

    local board = {}
    local sx, sy

    for i = 1, n do
        board[i] = io.read("*l")
        for j = 1, m do
            if board[i]:sub(j, j) == "T" then
                sx = i
                sy = j
            end
        end
    end

    local ans = BFS(board, n, m, sx, sy)

    if ans == -1 then
        print("Gamora")
    else
        print(ans)
    end
end

main()