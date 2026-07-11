local keyboard = {
    {'`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='},
    {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'},
    {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\''},
    {'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'}
}

map = {} -- teclas mapeadas com desvio para esquerda

-- mapeada todas as teclas (exceto as primeiras) como a tecla anterior
-- W vira Q, G vira F e assim por diante.
for i = 1, #keyboard do 
    for j = 2, #keyboard[i] do
        local key = keyboard[i][j]
        local pre = keyboard[i][j - 1]
        map[key] = pre
    end
end 

-- mapeaia as primeiras teclas a esquerda do teclado como elas mesmas.
for i = 1, #keyboard do
    local key = keyboard[i][1]
    map[key] = key
end

map[" "] = " " -- espaco continua igual kk.

local function main()
    while true do 
        local line = io.read()
        if line == nil then break end

        local ans = ""
        for i = 1, #line do 
            local char = line:sub(i, i)
            ans = ans .. map[char]
        end
        print(ans)
    end
end 

main()