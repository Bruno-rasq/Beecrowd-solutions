 
-- (%d+)          -- inteiro positivo
-- ([%-]?%d+)     -- inteiro com sinal opcional
-- (%S+)          -- qualquer token separado por espaço
-- (%a+)          -- palavra

local a, b, c = io.read():match("(%S+) (%S+) (%S+)")
a, b, c = tonumber(a), tonumber(b), tonumber(c)

local triangle = (a * c) / 2.0
local square = (b * b)
local rectangle = (a * b)
local circle = (c * c) * 3.14159
local trapeziu = ((a + b) * c) / 2.0 

print("TRIANGULO: " .. string.format("%.3f", triangle))
print("CIRCULO: " .. string.format("%.3f", circle))
print("TRAPEZIO: " .. string.format("%.3f", trapeziu))
print("QUADRADO: " .. string.format("%.3f", square))
print("RETANGULO: " .. string.format("%.3f", rectangle))