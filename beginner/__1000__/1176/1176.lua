local fib = {0, 1}
for i = 3, 63 do
    fib[i] = fib[i - 1] + fib[i - 2]
end

local T = io.read("*n")
for i=1, T do
    local n = io.read("*n")
    print(string.format("Fib(%d) = %d", n, fib[n + 1]))
end