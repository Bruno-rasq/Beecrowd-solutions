local function main()
    local pos = 0
    local sum = 0
    for i=1, 6 do
        local n = tonumber(io.read())
        if n >= 0 then
            pos = pos + 1 
            sum = sum + n
        end
    end
    print(string.format("%d valores positivos", pos))
    print(string.format("%.1f", sum / pos))
end

main()