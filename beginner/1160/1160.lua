local T = tonumber(io.read())

for i = 1, T do
    local A, B, TA, TB = io.read():match("(%S+) (%S+) (%S+) (%S+)")
    A, B, TA, TB = tonumber(A), tonumber(B), tonumber(TA), tonumber(TB)

    local time = 0
    while time <= 100 and A <= B do
        A = A + math.floor((A * TA) / 100)
        B = B + math.floor((B * TB) / 100)
        time = time + 1
    end

    if time > 100 then
        print("Mais de 1 seculo.")
    else
        print(string.format("%d anos.", time))
    end
end