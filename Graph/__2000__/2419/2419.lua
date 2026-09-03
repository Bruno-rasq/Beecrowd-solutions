-- delta para movimentos (cima, baixo, esquerda, direita)
local DELTA = {
    {-1, 0},
    { 1, 0},
    { 0,-1},
    { 0, 1}
}

local function inbounds(x, y, h, w)
    return x >= 1 and x <= h and y >= 1 and y <= w
end

local function countCoasts(map, height, width)
    local count = 0

    for row = 1, height do
        for col = 1, width do
            if map[row][col] == "#" then
                for i = 1, 4 do
                    local nx = row + DELTA[i][1]
                    local ny = col + DELTA[i][2]

                    if (not inbounds(nx, ny, height, width))
                        or map[nx][ny] == "." then
                        count = count + 1
                        break
                    end
                end
            end
        end
    end

    return count
end

local function main()
    local height, width = io.read("*n", "*n")
    io.read() -- consome o '\n'

    local map = {}

    for row = 1, height do
        local line = io.read()
        map[row] = {}

        for col = 1, width do
            map[row][col] = line:sub(col, col)
        end
    end

    print(countCoasts(map, height, width))
end

main()