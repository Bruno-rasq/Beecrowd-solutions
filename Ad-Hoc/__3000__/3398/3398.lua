local currenPark = tonumber(io.read())
local account = tonumber(io.read())

local ans = currenPark * account

print(string.format("%.2f", ans))