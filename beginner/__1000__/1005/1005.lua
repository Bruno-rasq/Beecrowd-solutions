local x = tonumber(io.read())
local y = tonumber(io.read())

local avg = (3.5 * x + 7.5 * y) / 11.0

print('MEDIA = ' .. string.format("%.5f", avg))