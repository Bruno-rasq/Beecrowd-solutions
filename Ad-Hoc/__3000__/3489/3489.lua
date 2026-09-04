INPUT = io.read("*l")
values = {}
for value in INPUT:gmatch("%S+") do
    table.insert(values, tonumber(value))
end

HASVALUE = false
TARGET = io.read("*n")
for i = 1, #values do
    for j = i + 1, #values do
        if(math.abs(values[i] + values[j] - TARGET) < 0.000000001) then
            print(string.format("%d %d %.0f", i - 1, j - 1, TARGET))
            HASVALUE = true
        end
    end
end

if not HASVALUE then print("null value") end