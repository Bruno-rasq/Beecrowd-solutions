local function bubbleSort(arr)
    for i = 1, #arr - 1 do
        for j = 1, #arr - i do
            if arr[j] < arr[j + 1] then
                local temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            end
        end
    end
    return arr
end

local x = io.read("*n")
local y = io.read("*n")
local z = io.read("*n")

local arr = bubbleSort({x, y, z})
local a, b, c = arr[1], arr[2], arr[3]

local a2 = a * a
local b2 = b * b
local c2 = c * c

if a >= b + c then
    print("NAO FORMA TRIANGULO")
else
    if a2 == b2 + c2 then
        print("TRIANGULO RETANGULO")
    end
    if a2 > b2 + c2 then
        print("TRIANGULO OBTUSANGULO")
    end
    if a2 < b2 + c2 then
        print("TRIANGULO ACUTANGULO")
    end
    if a == b and b == c then
        print("TRIANGULO EQUILATERO")
    end
    if (a == b and b ~= c) or (a == c and a ~= b) or (b == c and b ~= a) then
        print("TRIANGULO ISOSCELES")
    end
end