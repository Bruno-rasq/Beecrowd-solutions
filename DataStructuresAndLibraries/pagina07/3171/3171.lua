local visitado = {}
local grafo = {}
local qtdVisitados = 0

function dfs(grafo, visitado, u)
    visitado[u] = true
    qtdVisitados = qtdVisitados + 1

    for _, v in ipairs(grafo[u]) do
        if not visitado[v] then
            dfs(grafo, visitado, v)
        end
    end
end

local n, l = io.read("*n", "*n")

for i = 1, n do
    grafo[i] = {}
end

for i = 1, l do
    local x, y = io.read("*n", "*n")
    table.insert(grafo[x], y)
    table.insert(grafo[y], x)
end

dfs(grafo, visitado, 1)

if qtdVisitados == n then
    print("COMPLETO")
else
    print("INCOMPLETO")
end