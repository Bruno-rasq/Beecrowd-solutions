-- Comandos: 
-- D gira 90° para direita
-- E gira 90° para esquerda
-- F avança uma unidade

-- robot recebe uma serie de comandos e para capturar alguns itens
-- em um grid NxM, retorne quantos itens capturou.

local DELTAMOVES = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
local DELTAROTATE = { ["D"] = 1, ["E"] = -1}

local function ProcessProblem(N, M)

    local grid = {}
    local x = 0
    local y = 0
    local ans = 0
    local face = 0
    
    for i=1, N do
        local inputGridLine = io.read()
        local row = {}

        for j=1, M do
            row[#row + 1] = inputGridLine:sub(j, j)
            local cell = inputGridLine:sub(j, j)

            if cell == "N" or cell == "S" or cell == "O" or cell == "L" then
                x = i
                y = j
    
                if cell == "N" then face = 0 end
                if cell == "L" then face = 1 end
                if cell == "S" then face = 2 end
                if cell == "O" then face = 3 end
            end
        end

        grid[#grid + 1] = row
    end
    
    local commands = io.read()
    
    for i = 1, #commands do
        local cmd = commands:sub(i, i)
        
        if cmd == "F" then
            local nx = x + DELTAMOVES[face + 1][1]
            local ny = y + DELTAMOVES[face + 1][2]
    
            if nx >= 1 and nx <= N and ny >= 1 and ny <= M and grid[nx][ny] ~= "#" then
                if grid[nx][ny] == "*" then
                    ans = ans + 1
                    grid[nx][ny] = "."
                end
    
                x = nx
                y = ny 
            end
        else
            face = (face + DELTAROTATE[cmd] + 4) % 4
        end
    end
    
    print(ans)
end


local N, M, commandLength = io.read("*n", "*n", "*n")

while N ~= 0 or M ~= 0 or commandLength ~= 0 do
    io.read() -- consome o restante da linha
    ProcessProblem(N, M)
    N, M, commandLength = io.read("*n", "*n", "*n")
end
