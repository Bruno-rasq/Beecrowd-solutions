local a, b, c = io.read():match("(%S+) (%S+) (%S+)")
a, b, c = tonumber(a), tonumber(b), tonumber(c)

-- maiorAB = (a + b + abs(a - b)) / 2
local maior = (a + b + math.abs(a - b)) / 2
maior = (maior + c + math.abs(maior - c)) / 2

print(string.format("%.0f eh o maior", maior))