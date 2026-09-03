local a = tonumber(io.read())
local b = tonumber(io.read())
local c = tonumber(io.read())

local avg = (2 * a + 3 * b + 5 * c) / 10.0

print('MEDIA = ' .. string.format("%.1f", avg))