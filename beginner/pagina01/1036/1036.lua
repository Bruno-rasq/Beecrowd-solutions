local function bhaskara(a, b, delta)
    local r1 = (-b + math.sqrt(delta)) / (2 * a)
    local r2 = (-b - math.sqrt(delta)) / (2 * a)

    print(string.format("R1 = %.5f", r1))
    print(string.format("R2 = %.5f", r2))
end

local a, b, c = io.read():match("([%-]?%d+%.?%d*) ([%-]?%d+%.?%d*) ([%-]?%d+%.?%d*)")
a, b, c = tonumber(a), tonumber(b), tonumber(c)

local delta = (b * b) - (4 * a * c)

if a ~= 0 and delta >= 0 then
    bhaskara(a, b, delta)
else
    print("Impossivel calcular")
end