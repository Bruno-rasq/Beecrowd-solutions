-- Deslocamentos conforme a direção do robô.
local DELTA = {
    U = {-1,  0},
    D = { 1,  0},
    L = { 0, -1},
    R = { 0,  1}
}

-- Ordem de verificação: frente, esquerda e direita.
local ADJ = {
    U = {"U", "L", "R"},
    D = {"D", "L", "R"},
    L = {"L", "U", "D"},
    R = {"R", "U", "D"}
}

-- Converte uma mudança de direção em um comando (L ou R).
local function rotate(curr, adj)
    local rot = {
        U = {L = "L", R = "R"},
        D = {L = "R", R = "L"},
        L = {U = "R", D = "L"},
        R = {U = "L", D = "R"}
    }
    return rot[curr][adj]
end

-- Percorre todo o caminho.
local function travel(board, n, m, robotX, robotY)
    local commands = {}
    local robot = {direction = "D", coord = {x = robotX,y = robotY}}
    local move = false
    board[robotX][robotY] = "1" -- Marca a posição inicial como visitada.
    repeat
        move = false
        for _, adj in ipairs(ADJ[robot.direction]) do
            local nx = robot.coord.x + DELTA[adj][1]
            local ny = robot.coord.y + DELTA[adj][2]

            if nx >= 1 and nx <= n and ny >= 1 and ny <= m and board[nx][ny] == "0" then
                if adj ~= robot.direction then -- verifica se precisa rotacionar antes.
                    table.insert(commands, rotate(robot.direction, adj))
                end
                table.insert(commands, "F")    -- segue em frente
                robot.direction = adj          -- atualiza a direção do robo.
                robot.coord.x = nx             -- atualiza coordenada x do robo.
                robot.coord.y = ny             -- atualiza coordenada y do robo.
                board[nx][ny] = "1"            -- marca pos anterior como bloqueada
                move = true                    -- registra que houve movimento.
                break                          -- não continua a executar as adjs 
            end
        end
    until not move
    table.insert(commands, "E")
    return table.concat(commands, " ")
end

local function main()
    while true do
        local input = io.read()
        if not input then break end 
        
        local n, m = input:match("(%d+) (%d+)")
        n,m = tonumber(n), tonumber(m)
        
        local robotx, roboty
        local board = {}

        for i = 1, n do
            local row = {}
            local col = 1
            for token in io.read():gmatch("%S+") do
                row[col] = token
                if token == "X" then
                    robotx = i
                    roboty = col
                end
                col = col + 1
            end
            board[i] = row
        end
        print(travel(board, n, m, robotx, roboty))
    end
end

main()