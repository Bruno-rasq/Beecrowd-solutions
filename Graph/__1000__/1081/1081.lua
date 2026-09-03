local function DFSr(graph, node, rspace)
    graph[node].visited = true
    local path = false
    local space = string.rep(" ", rspace)

    for i = 1, #graph[node].childrens do
        local child = graph[node].childrens[i]
        path = true
        if not graph[child].visited then
            print(string.format("%s%d-%d pathR(G,%d)", space, node, child, child))
            DFSr(graph, child, rspace + 2)
        else
            print(string.format("%s%d-%d", space, node, child))
        end
    end

    return path
end


local N = tonumber(io.read())
for caso = 1, N do
    local nodes, conn = io.read("*n", "*n")

    local graph = {}
    for j = 0, nodes - 1 do
        graph[j] = {visited = false, childrens = {}}
    end

    for j = 1, conn do
        local node, child = io.read("*n", "*n")
        table.insert(graph[node].childrens, child)
    end

    -- O Python percorre os destinos em ordem crescente
    for node = 0, nodes - 1 do
        table.sort(graph[node].childrens)
    end

    print(string.format("Caso %d:", caso))
    for node = 0, nodes - 1 do
        if not graph[node].visited then
            local path = DFSr(graph, node, 2)
            if path then print() end
        end
    end
end