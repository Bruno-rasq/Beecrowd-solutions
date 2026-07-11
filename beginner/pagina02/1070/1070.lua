local function main()
    local n = tonumber(io.read())
    local count = 0
    while count < 6 do
        if n % 2 ~= 0 then 
            print(n)
            count = count + 1
        end 
        n = n + 1
    end
end

main()