local x1, y1 = io.read():match("(%S+) (%S+)")
local x2, y2 = io.read():match("(%S+) (%S+)")
x1, y1, x2, y2 = tonumber(x1),tonumber(y1), tonumber(x2), tonumber(y2)

local dist = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

print(string.format("%.4f", dist))