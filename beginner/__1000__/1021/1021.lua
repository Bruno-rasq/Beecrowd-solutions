local notas = {10000, 5000, 2000, 1000, 500, 200}
local moedas = {100, 50, 25, 10, 5, 1}

local reais, centavos = io.read():match("(%d+)%.(%d+)")
reais, centavos = tonumber(reais), tonumber(centavos)

reais = reais * 100 + centavos

print("NOTAS:")
for _, value in ipairs(notas) do
    local n = reais // value
    print(string.format("%d nota(s) de R$ %.2f", n, value / 100))
    reais = reais % value
end

print("MOEDAS:")
for _, value in ipairs(moedas) do
    local m = reais // value
    print(string.format("%d moeda(s) de R$ %.2f", m, value / 100))
    reais = reais % value
end