-- Grafo: chave (node) -> lista de nodes conectados.
local Graph = {}

-- Insere uma nova aresta no grafo.
local function AddEdge(source, target)
    if Graph[source] == nil then
        Graph[source] = {}
    end
    table.insert(Graph[source], target)
end

-- Copia uma lista.
local function copy(list)
    local c = {}
    for i = 1, #list do
        c[i] = list[i]
    end
    return c
end

-- Busca em largura.
-- Retorna a quantidade de arestas do menor caminho entre source e target.
local function BFS(source, target)
    local head = 1
    local queue = {}
    local visited = {}

    table.insert(queue, { source = source, path = {}})
    visited[source] = true

    while head <= #queue do
        local curr = queue[head]
        head = head + 1

        if curr.source == target then return #curr.path end
        local adj = Graph[curr.source]
        if adj then
            for i = 1, #adj do
                local node = adj[i]
                if not visited[node] then
                    visited[node] = true

                    local nextpath = copy(curr.path)
                    table.insert(nextpath, node)

                    table.insert(queue, {source = node, path = nextpath})
                end
            end
        end
    end
    return -1
end

local function main()

    local nodes, edges = io.read("*n", "*n")
    io.read() -- Consome o fim da linha deixado pelo *n

    -- Lê todas as arestas.
    for i = 1, edges do
        local nodeA, nodeB = io.read():match("(%S+) (%S+)")
        AddEdge(nodeA, nodeB)
        AddEdge(nodeB, nodeA)
    end

    local costToCheese = BFS("Entrada", "*")
    local costToOut = BFS("*", "Saida")

    print(costToCheese + costToOut)
end

main()