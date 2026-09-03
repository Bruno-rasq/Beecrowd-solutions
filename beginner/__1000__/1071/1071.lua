local function main()
    local x = tonumber(io.read())
    local y = tonumber(io.read())
    local max = math.max(x, y)
    local min = math.min(x, y)
    local count = 0
    for i = min + 1, max - 1 do
        if i % 2 ~= 0 then
            count = count + i
        end
    end
    print(count)
end

main()