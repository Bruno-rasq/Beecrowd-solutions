local a = io.read("*n")
local b = io.read("*n")
local c = io.read("*n")

local perimeter = a + b + c
local area = ((a + b) * c) / 2.0
local cond = a < (b + c) and b < (a + c) and c < (b + a)

if cond then
    print(string.format("Perimetro = %.1f", perimeter))
else
    print(string.format("Area = %.1f", area))
end