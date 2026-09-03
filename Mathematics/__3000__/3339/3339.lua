local n = tonumber(io.read())

for i = 1, n do
    local xi, xf = io.read("*n", "*n")

    local ans

    if xi == 0 then
        ans = math.floor(math.sqrt(xf)) + 1
    else
        ans = math.floor(math.sqrt(xf))
            - math.floor(math.sqrt(xi - 1))
    end

    print(ans)
end