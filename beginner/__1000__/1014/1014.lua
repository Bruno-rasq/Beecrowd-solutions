local km = tonumber(io.read())
local fuel = tonumber(io.read())
local consumption = km / fuel 

print(string.format("%.3f km/l", consumption))