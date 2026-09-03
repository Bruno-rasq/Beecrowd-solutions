local employerName = io.read()
local salaryFixed = tonumber(io.read())
local solds = tonumber(io.read())

local commision = (solds * 15) / 100
local total = salaryFixed + commision

print("TOTAL = R$ " .. string.format("%.2f", total))