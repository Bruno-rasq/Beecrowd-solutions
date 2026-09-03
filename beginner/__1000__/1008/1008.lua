local ID = tonumber(io.read())
local salaryBase = tonumber(io.read())
local valorPerHour = tonumber(io.read())

local total = (salaryBase * valorPerHour)

print('NUMBER = ' .. ID)
print('SALARY = U$ ' .. string.format("%.2f", total))