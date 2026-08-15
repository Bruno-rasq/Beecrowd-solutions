while true do
    local input = io.read("*l")
    
    local n, m = input:match("(%S+) (%S+)")
    n, m = tonumber(n), tonumber(m)
    
    if n <= 0 or m <= 0 then break end 
    
    local min = math.min(n, m)
    local max = math.max(n, m)

    local ans = ""
    local sum = 0
    for i=min, max do
        ans = ans .. string.format("%d", i) .. " "
        sum = sum + i
    end

    ans = ans .. "Sum=" .. string.format("%d", sum)
    print(ans)
end