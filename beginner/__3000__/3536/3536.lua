local arco = 0
local escudo = 0
local espada = 0
local pocao = 0

local n = io.read("*n")
for i=1, n do
    local item = io.read()

    if item == "arco" then arco  = arco + 1 end 
    if item == "escudo" then escudo = escudo + 1 end
    if item == "espada" then espada = espada + 1 end
    if item == "pocao" then pocao = pocao + 1 end 
end

print(string.format("arco %d", arco))
print(string.format("escudo %d", escudo))
print(string.format("espada %d", espada + 1))
print(string.format("pocao %d", pocao))