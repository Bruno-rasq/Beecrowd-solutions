function isPrime(n)
    if n <= 1 then return false end -- Números menores ou iguais a 1 não são primos
    if n == 2 then return true end -- O único número par que é primo é o 2
    if n % 2 == 0 then return false end -- Exclui os outros números pares
    local limite = math.sqrt(n) -- Testa a divisão pelos ímpares até a raiz quadrada do número
    for i = 3, limite, 2 do
        if n % i == 0 then
            return false -- Achou um divisor, não é primo
        end
    end
    return true -- Se não achou divisores, é primo
end

local function counting(nums, jump)
    local idx = #nums
    local sum = 0
    while idx >= 1 do
        sum = sum + nums[idx]
        idx = idx - jump
    end
    return sum
end

while true do
    line = io.read()
    if line == nil then break end
    local n = tonumber(line)
    local nums = {}
    for i=1, n do
        table.insert(nums, tonumber(io.read()))
    end
    local jump = tonumber(io.read())
    local ans = isPrime(counting(nums, jump))

    if ans then 
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else
        print("Bad boy! I’ll hit you.")
    end
end