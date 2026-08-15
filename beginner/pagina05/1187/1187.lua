local OPE = io.read()
local GRD = {}
local FLA = 1
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

for i = 1, 6 do
    if FLA == FLB then break end
    for j = 1, 12 do
        if j > FLA and j < FLB then 
            SUM = SUM + GRD[i][j]
            CNT = CNT + 1
        end
    end
    FLA = FLA + 1
    FLB = FLB - 1
end

if OPE == "M" then 
    SUM = SUM / CNT 
end
print(string.format("%.1f", SUM))