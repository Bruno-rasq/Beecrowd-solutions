local temp = tonumber(io.read())
local vel = tonumber(io.read())
local fuel = (temp * vel) / 12.0

print(string.format("%.3f", fuel))