local function main()
    local n = tonumber(io.read())
    local INI = 0
    local OUT = 0
    for i=1, n do
        local x = tonumber(io.read())
        if x >= 10 and x <= 20 then 
            INI = INI + 1 
        else 
            OUT = OUT + 1 
        end
    end
    print(string.format("%d in", INI))
    print(string.format("%d out", OUT))
end

main()