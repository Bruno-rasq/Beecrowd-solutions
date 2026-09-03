local function main()
    local n = tonumber(io.read())
    for i=1, n do
        if i % 2 ~= 0 then print(i) end
    end
end

main()