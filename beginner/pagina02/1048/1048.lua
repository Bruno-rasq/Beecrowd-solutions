local salary = io.read("*n")
local increasy = 0

if salary <= 400.00 then increasy = 15 end
if salary >= 400.01 and salary <= 800.00 then increasy = 12 end
if salary >= 800.01 and salary <= 1200.00 then increasy = 10 end
if salary >= 1200.01 and salary <= 2000.00 then increasy = 7 end 
if salary > 2000.00 then increasy = 4 end 

local reajust = (salary * increasy) / 100.00
local salary = salary + reajust

print(string.format("Novo salario: %.2f", salary))
print(string.format("Reajuste ganho: %.2f", reajust))
print("Em percentual: " .. increasy .. " %")