local n, s = io.read("*n", "*n")
local frequence = {}
local countpairs = 0

for i = 1, n do
    local curr = io.read("*n")
    local need = s - curr

    countpairs = countpairs + (frequence[need] or 0)
    frequence[curr] = (frequence[curr] or 0) + 1
end

print(countpairs)