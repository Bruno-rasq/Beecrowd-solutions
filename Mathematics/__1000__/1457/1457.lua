local function countExclamation(line)
    local count = 0
    for _ in string.gmatch(line, "!") do
        count = count + 1
    end
    return count
end

local function OOA()
    local inp = io.read()
    local K = countExclamation(inp)
    local N = tonumber(string.sub(inp, 1, #inp - K))
    local ans = N
    local mul = 1
    while true do
        local _next = ans * (N - (mul * K))
        if _next <= 0 then break end
        ans = _next
        mul = mul + 1
    end
    print(ans)
end

local t = tonumber(io.read())
for i=1, t do
    OOA()
end