local a = io.read("*n")
local b = io.read("*n")
local c = io.read("*n")

local function bubbleSort(lista)
    for i = 1, #lista - 1 do
        for j = 1, #lista - i do
            if lista[j] > lista[j + 1] then
                local temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
            end
        end
    end
    return lista
end

local sortedlist = bubbleSort({a, b, c})

for i = 1, #sortedlist do
    print(sortedlist[i])
end

print("")

print(a)
print(b)
print(c)