local graph = {}
graph["vertebrado ave carnivoro"] = "aguia"
graph["vertebrado ave onivoro"] = "pomba"
graph["vertebrado mamifero onivoro"] = "homem"
graph["vertebrado mamifero herbivoro"] = "vaca"
graph["invertebrado inseto hematofago"] = "pulga"
graph["invertebrado inseto herbivoro"] = "lagarta"
graph["invertebrado anelideo hematofago"] = "sanguessuga"
graph["invertebrado anelideo onivoro"] = "minhoca"
local a = io.read()
local b = io.read()
local c = io.read()
local key = a .. " " .. b .. " " .. c

print(graph[key])
