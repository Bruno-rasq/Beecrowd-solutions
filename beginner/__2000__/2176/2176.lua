local segment = io.read()

local bits_1 = 0
for i = 1, #segment do 
    local bit = segment:sub(i, i)
    if bit == "1" then
        bits_1 = bits_1 + 1
    end
end

if bits_1 % 2 == 0 then
    segment = segment .. "0"
else 
    segment = segment .. "1"
end

print(segment)