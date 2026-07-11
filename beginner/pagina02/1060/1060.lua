local pos = 0

for i=1, 6 do
    local n = tonumber(io.read())
    if n >= 0 then
        pos = pos + 1
    end
end

print(string.format("%d valores positivos", pos))