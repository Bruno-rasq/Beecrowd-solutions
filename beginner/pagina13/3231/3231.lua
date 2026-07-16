local INFINIT = math.huge

local n, h, l = io.read("*n", "*n", "*n")

-- Armazena na lista os IDs dos filmes ruins
local horror_list = {}
for i = 1, h do
    table.insert(horror_list, io.read("*n"))
end

-- Cria o grafo com os IDs de todos os filmes
-- e alimenta o vetor de distância com todos os valores iguais a Infinito
local graph = {}
local dists = {}
for id = 0, n - 1 do
    graph[id] = {}
    dists[id] = INFINIT
end

-- Todos os filmes que pertencem à lista de horror têm H = 0
-- Adiciona os filmes da lista na fila para serem processados.
local queue = {}
for i = 1, h do
    dists[horror_list[i]] = 0
    table.insert(queue, horror_list[i])
end

-- Alimenta o grafo com os nós vizinhos em ambos os sentidos
for i = 1, l do
    local a, b = io.read("*n", "*n")
    table.insert(graph[a], b)
    table.insert(graph[b], a)
end

-- Busca em largura (BFS multi-source)
local head = 1
while head <= #queue do
    local curr = queue[head]
    head = head + 1

    for i = 1, #graph[curr] do
        local v = graph[curr][i]

        if dists[v] == INFINIT then
            dists[v] = dists[curr] + 1
            table.insert(queue, v)
        end
    end
end

-- Busca o maior Horror Index
local maxH = dists[0]
for i = 1, n - 1 do
    if dists[i] > maxH then
        maxH = dists[i]
    end
end

-- Em caso de empate, o menor ID vence
for i = 0, n - 1 do
    if dists[i] == maxH then
        print(i)
        break
    end
end