local function main()
    local pos = 0
    for i=1, 5 do
        local n = tonumber(io.read())
        if n % 2 == 0 then
            pos = pos + 1 
        end
    end
    print(string.format("%d valores pares", pos))
end

main()