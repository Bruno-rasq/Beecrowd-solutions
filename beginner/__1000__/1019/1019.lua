local value = tonumber(io.read())
local hor = math.floor(value / 3600)
local min = math.floor((value - (hor * 3600)) / 60)
local seg = value % 60

print(string.format("%d:%d:%d", hor, min, seg))