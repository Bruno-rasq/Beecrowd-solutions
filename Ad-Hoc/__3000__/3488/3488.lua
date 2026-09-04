-- Números que são potência de 2 possuem apenas um bit 1 em uma forma binaria.
-- 8 por exm: 0b1000,

-- Quando se remove 1 do valor, todos os bits que eram 0 viram 1 e vice-versa.
-- 7 por exemplo 0b0111.

-- A operação AND (&) compar pares de bits, se ambos forem 1 então é 1 senão 0.
-- quando se compara os bits de um valor pelo seu anterio, se o resultado for 0.
-- então o número é potência de 3.

local function isPowerOfTwo(x)
    if x and  x > 0 and ((x & (x - 1)) == 0) then return "true" end
    return "false"
end

local n = io.read("*n")
print(isPowerOfTwo(n))