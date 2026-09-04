local t = tonumber(io.read())
for i=1, t do
    local n, m = io.read("*n", "*n")
    local ans = math.ceil((n - 2) / 3) * math.ceil((m - 2) / 3)
    print(ans)
end