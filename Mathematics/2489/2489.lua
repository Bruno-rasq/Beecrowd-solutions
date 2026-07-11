local PI = math.acos(-1)

while true do
    local A, D, R = io.read("*n", "*n", "*n")
    if A == nil then
        break
    end

    local rad = R * PI / 180
    local H = A - D / math.tan(rad)

    print(string.format("%.4f", H))
end