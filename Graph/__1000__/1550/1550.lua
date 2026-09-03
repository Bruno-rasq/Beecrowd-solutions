-- Inverte os dígitos do número, ignorando os zeros à esquerda
local function invertion(num)
    local inverted = 0
    while num > 0 do
        local digit = num % 10
        inverted = (inverted * 10) + digit
        num = math.floor(num / 10)
    end
    return inverted
end

-- Incrementa em 1 o valor recebido
local function increment(num)
    return num + 1
end

-- Carrossel de funções
local MATH = {
    invertion,
    increment
}

-- BFS procurando a quantidade mínima de operações
local function BFS(source, target, MATH)
    local queue = {}
    local visiteds = {}
    local head = 1

    queue[#queue + 1] = {value = source, steps = 0}

    visiteds[source] = true

    while head <= #queue do
        local curr = queue[head]
        head = head + 1
        if curr.value == target then return curr.steps end

        for _, func in ipairs(MATH) do
            local nextValue = func(curr.value)
            if not visiteds[nextValue] then
                queue[#queue + 1] = {value = nextValue, steps = curr.steps + 1}
                visiteds[nextValue] = true
            end
        end
    end
    return -1
end

local T = tonumber(io.read())
for i = 1, T do
    local source, target = io.read("*n", "*n")
    local ans = BFS(source, target, MATH)
    print(ans)
end