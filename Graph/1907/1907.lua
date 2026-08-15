local DELTAS = {
    {-1,  0},
    { 1,  0},
    { 0, -1},
    { 0,  1}
}

local HEIGHT, WIDTH = io.read("*n", "*n")
io.read("*l") -- Descarta a quebra de linha após os números.

local grid = {}
local colors = 0

-- Lê a matriz e converte cada linha em uma tabela de caracteres.
-- Complexidade: O(HEIGHT × WIDTH)
for i = 1, HEIGHT do
    local line = io.read("*l")
    grid[i] = {}

    for j = 1, WIDTH do
        grid[i][j] = line:sub(j, j)
    end
end

-- Percorre toda a matriz. Sempre que encontra uma célula branca ainda
-- não visitada ('.'), inicia uma BFS para pintar toda a componente conexa.
-- Cada célula é visitada apenas uma vez.
-- Complexidade total: O(HEIGHT × WIDTH)
for i = 1, HEIGHT do
    for j = 1, WIDTH do
        if grid[i][j] == "." then
            colors = colors + 1
            grid[i][j] = "o"

            local queue = {{x = i, y = j}}
            local head = 1

            while head <= #queue do
                local curr = queue[head]
                head = head + 1

                for _, delta in ipairs(DELTAS) do
                    local nx = curr.x + delta[1]
                    local ny = curr.y + delta[2]

                    if nx >= 1 and nx <= HEIGHT and
                       ny >= 1 and ny <= WIDTH and
                       grid[nx][ny] == "." then

                        grid[nx][ny] = "o"
                        queue[#queue + 1] = {x = nx, y = ny}
                    end
                end
            end
        end
    end
end

print(colors)