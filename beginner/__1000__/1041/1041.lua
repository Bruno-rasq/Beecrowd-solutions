local x = io.read("*n")
local y = io.read("*n")
local ans = "Origem"

if x > 0 and y > 0 then
    ans = "Q1"
elseif x > 0 and y < 0 then
    ans = "Q4"
elseif x < 0 and y > 0 then
    ans = "Q2"
elseif x < 0 and y < 0 then
    ans = "Q3"
elseif x == 0 and y ~= 0 then
    ans = "Eixo Y"
elseif x ~= 0 and y == 0 then
    ans = "Eixo X"
end

print(ans)