local N = io.read("*n")
local M = io.read("*n")

local impossible = false
local visiteds = {}

local GRAPH = {}

for i = 1, N do
    GRAPH[i] = {
        value = io.read("*n"),
        conn = {}
    }

    visiteds[i] = false
end

for i = 1, M do
    local a = io.read("*n") + 1
    local b = io.read("*n") + 1

    table.insert(GRAPH[a].conn, b)
    table.insert(GRAPH[b].conn, a)
end

for i = 1, N do
    if not visiteds[i] then

        local sum = 0
        local stack = {i}

        visiteds[i] = true

        while #stack > 0 do
            local node = table.remove(stack)

            sum = sum + GRAPH[node].value

            for _, neighbor in ipairs(GRAPH[node].conn) do
                if not visiteds[neighbor] then
                    visiteds[neighbor] = true
                    stack[#stack + 1] = neighbor
                end
            end
        end

        if sum < 0 then
            impossible = true
            break
        end
    end
end

print(impossible and "IMPOSSIBLE" or "POSSIBLE")