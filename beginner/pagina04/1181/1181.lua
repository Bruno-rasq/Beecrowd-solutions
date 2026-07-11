local line = tonumber(io.read()) + 1 -- +1 para acertar a indexação-0
local operation = io.read() -- S para soma e M para media
local grid = {} -- grid 12x13

for r=1, 12 do
    local row = {}
    for c=1, 12 do
        row[c] = tonumber(io.read())
    end
    grid[r] = row
end

local sum = 0
for i=1, 12 do
    sum = sum + grid[line][i]
end

if operation == "S" then print(sum) end
if operation == "M" then print(sum / 12) end 