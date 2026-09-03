local OPE = io.read()
local GRD = {}
local FLB = 12
local SUM = 0
local CNT = 0

-- lê os dados do grid
for i=1, 12 do
    local line = {}
    for j=1, 12 do
        table.insert(line, tonumber(io.read()))
    end
    table.insert(GRD, line)
end

for i = 1, 12 do
    for j = 1, 12 do
        if j < FLB then 
            SUM = SUM + GRD[i][j]
            CNT = CNT + 1
        end
    end
    FLB = FLB - 1
end

if OPE == "M" then 
    SUM = SUM / CNT 
end
print(string.format("%.1f", SUM))