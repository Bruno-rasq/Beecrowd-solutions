-- Função que gera uma estrtura de nó para a Árvore binária
local function newNode(value)
    return {
        value = value,    -- valor do nó
        left = nil,       -- nó da esquerda
        right = nil       -- nó da direita
    }
end

-- Função que insere um novo nó ana árvore binária.
local function insert(node, value)
    
    if node == nil then return newNode(value) end

    if value < node.value then
        node.left = insert(node.left, value)
    else
        node.right = insert(node.right, value)
    end
    
    return node
end

-- Registra a árvore binária em suas três formas.
local function preOrder(result, node)
    if node == nil then return end

    result[#result + 1] = node.value
    preOrder(result, node.left)
    preOrder(result, node.right)
end

local function inOrder(result, node)
    if node == nil then return end

    inOrder(result, node.left)
    result[#result + 1] = node.value
    inOrder(result, node.right)
end

local function posOrder(result, node)
    if node == nil then return end

    posOrder(result, node.left)
    posOrder(result, node.right)
    result[#result + 1] = node.value
end

local testCase = tonumber(io.read())
for t=1, testCase do
    local n = io.read()
    local root = nil -- nó raiz da árvore.
    for value in io.read():gmatch("%S+") do
        root = insert(root, tonumber(value))
    end

    print(string.format("Case %d:", t))

    local PRO = {}
    preOrder(PRO, root)
    print(string.format("Pre.: %s", table.concat(PRO, " ")))
    
    local INO = {}
    inOrder(INO, root)
    print(string.format("In..: %s", table.concat(INO, " ")))
    
    local POO = {}
    posOrder(POO, root)
    print(string.format("Post: %s", table.concat(POO, " ")))

    print() -- linha em branco
end