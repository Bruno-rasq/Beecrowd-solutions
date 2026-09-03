local prices = {4.00, 4.50, 5.00, 2.00, 1.50}

local code, qnt = io.read():match("(%d+) (%d+)")
code = tonumber(code)
qnt = tonumber(qnt)

local total = prices[code] * qnt

print(string.format("Total: R$ %.2f", total))