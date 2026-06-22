 
-- (%d+)          -- inteiro positivo
-- ([%-]?%d+)     -- inteiro com sinal opcional
-- (%S+)          -- qualquer token separado por espaço
-- (%a+)          -- palavra

local total = 0

while true do
    local input = io.read()
    if input == nil then
        break
    end

    local _, quantity, price = input:match("(%d+) (%d+) ([%d%.]+)")

    quantity = tonumber(quantity)
    price = tonumber(price)

    total = total + (price * quantity)
end

print("VALOR A PAGAR: R$ " .. string.format("%.2f", total))