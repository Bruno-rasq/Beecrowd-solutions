-- DFS visita todos os familiares de um individuo A e marca-os como visitados.
local function DFS(nome, id)
    NOMES[nome].visitado = true

    for _, familiarID in ipairs(grafo[id]) do
        local familiarNome = IDS[familiarID]

        if not NOMES[familiarNome].visitado then
            DFS(familiarNome, familiarID)
        end
    end
end

local N, M = io.read("*n", "*n")
io.read() -- consome o '\n' restante

local id = 1
local familias = 0
NOMES = {}   -- nome -> {ID, visitado}
IDS = {}     -- ID -> nome
grafo = {}   -- ID -> lista de vizinhos

for i = 1, M do
    local A, _, B = io.read():match("(%S+) (%S+) (%S+)")

    -- cadastra A se necessário
    if not NOMES[A] then
        NOMES[A] = {
            ID = id,
            visitado = false
        }
        IDS[id] = A
        grafo[id] = {}
        id = id + 1
    end
    -- cadastra B se necessário
    if not NOMES[B] then
        NOMES[B] = {
            ID = id,
            visitado = false
        }
        IDS[id] = B
        grafo[id] = {}
        id = id + 1
    end

    local idA = NOMES[A].ID
    local idB = NOMES[B].ID
    table.insert(grafo[idA], idB)
    table.insert(grafo[idB], idA)
end

for id, nome in pairs(IDS) do
    if not NOMES[nome].visitado then
        familias = familias + 1
        DFS(nome, id)
    end
end

print(familias)