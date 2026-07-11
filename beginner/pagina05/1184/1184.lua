local operation = io.read() -- S para soma e M para media
local grid = {} -- grid 12x13

for r=1, 12 do
    local row = {}
    for c=1, 12 do
        row[c] = tonumber(io.read())
    end
    grid[r] = row
end

local count = 0
local sum = 0
for row=1, 12 do
    for col=1, 12 do
        if col < row then 
            sum = sum + grid[row][col]
            count = count + 1
        end
    end
end

if operation == "S" then print(string.format("%.1f", sum)) end
if operation == "M" then 
    print(string.format("%.1f", sum / count))
end