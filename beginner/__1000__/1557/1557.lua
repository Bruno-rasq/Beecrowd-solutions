while true do
    local N = tonumber(io.read())
    if N == 0 then break end

    -- Maior valor da matriz: 2^(2 * (N - 1))
    local MAXVALUE = 2 ^ (2 * (N - 1))
    local size = tostring(MAXVALUE)
    local col = 1
    local row = 1

    for i = 1, N do
        local output = ""
        for j = 1, N do
            local value = tostring(col)
            -- Preenche com espaços à esquerda
            while #value < #size - 2 do
                value = " " .. value
            end
            output = output .. value
            if j ~= N then output = output .. " " end
            col = col * 2
        end

        print(output)
        row = row * 2
        col = row
    end
    print()
end