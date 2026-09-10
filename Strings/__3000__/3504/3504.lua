-- VERIFICANDO PALÍNDROMOS USANDO A TÉCNICA DOS DOIS PONTEIROS
-- A IDEIA É CRIAR UM PONTEIRO PARA O PRIMEIRO E ULTIMO CARACTER
-- DA PALAVRA/FRASE, SE FOREM IGUAIS ENTÃO AUMENTA EM 1 O PONTEIRO
-- DA ESQUERDA E REDUZ EM 1 O PONTEIRO DA DIREITA.
-- DO CONTRÁRIO ENCERRA A VERIFICAÇÃO.
-- O LOOP ACABA QUANDO AMBOS OS PONTEIROS APONTAREM PARA O MESMO 
-- INDICE.
local function CHECKPALINDROME(word)
    local LEFT = 1
    local RIGHT = #word

    while LEFT < RIGHT do
        if word:sub(LEFT, LEFT) ~= word:sub(RIGHT, RIGHT) then
            return false
        end
        LEFT = LEFT + 1
        RIGHT = RIGHT - 1
    end

    return true
end

local word = io.read()

if CHECKPALINDROME(word) then
    print(string.format("A frase [%s] eh palindrome", word))
else
    print(string.format("A frase [%s] nao eh palindrome", word))
end