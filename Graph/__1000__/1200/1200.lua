local function Node(value)
    return {value = value, left = nil, right = nil}
end

local function insert(node, value)
    if node == nil then return Node(value) end
    if value < node.value then node.left = insert(node.left, value) end
    if value > node.value then node.right = insert(node.right, value) end
    return node
end

local function search(node, value)
    if node == nil then return false end
    if node.value == value then return true end
    if value < node.value then return search(node.left, value) end
    if value > node.value then return search(node.right, value) end
end

local first

local function PREFIX(node)
    if node == nil then return end

    if not first then io.write(" ") end
    io.write(string.char(node.value))
    first = false

    PREFIX(node.left)
    PREFIX(node.right)
end

local function INFIX(node)
    if node == nil then return end

    INFIX(node.left)

    if not first then io.write(" ") end
    io.write(string.char(node.value))
    first = false

    INFIX(node.right)
end

local function POSFIX(node)
    if node == nil then return end

    POSFIX(node.left)
    POSFIX(node.right)

    if not first then io.write(" ") end
    io.write(string.char(node.value))
    first = false
end


local root = nil -- raiz da árvore binaria.

while true do

    local input = io.read()
    if input == nil then break end

    if input == "PREFIXA" and root ~= nil then
        first = true
        PREFIX(root)
        io.write("\n")

    elseif input == "INFIXA" and root ~= nil then
        first = true
        INFIX(root)
        io.write("\n")

    elseif input == "POSFIXA" and root ~= nil then
        first = true
        POSFIX(root)
        io.write("\n")

    else

        local operation = input:sub(1, 1)
        local char = input:sub(3, 3)

        if operation == "I" then
            root = insert(root, string.byte(char))
        end

        if operation == "P" then
            local response = search(root, string.byte(char))
            io.write(char)

            if response then
                io.write(" existe\n")
            else
                io.write(" nao existe\n")
            end
        end
    end
end