local function evenOrOdd(n)
    if(n == 0) then return "NULL" end
    if(n % 2 == 0) then
        if (n > 0) then return "EVEN POSITIVE" end
        return "EVEN NEGATIVE" 
    end
    if(n > 0) then return "ODD POSITIVE" end
    return "ODD NEGATIVE"
end

t = tonumber(io.read())

for i=1, t do
    local n = tonumber(io.read())
    print(evenOrOdd(n))
end