for i=1, 100 do
    local n = tonumber(io.read())
    if n <= 10 then 
        print(string.format("A[%d] = %.1f", i - 1, n))
    end
end