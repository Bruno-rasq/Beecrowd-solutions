-- Cada inteiro N representa uma segmento de uma fita de leds com <= 50 leds
-- os bits que compõe este valor representam cada led do segmento no qual
-- 1(led apagado) - 0(acesso).

-- São necessários um inteiro com 8bytes (64bits) para compor os leds desta
-- fita. O código simplesmente executa uma operação bit a bit lendo cada bit
-- de N e buscando a maior sequência de bits 1 

local function main()
    local buffer = {}
    local n = io.read("*n")
    for i=1, n do
        local leds = io.read("*n")
        local maxs = 0
        local curs = 0
        for i=0, 63 do 
            if (leds & (1 << i)) ~= 0 then 
                curs = curs + 1
                maxs = math.max(curs, maxs)
            else
                curs = 0
            end
        end
        table.insert(buffer, maxs)
    end
    print(table.concat(buffer, "\n"))
end

main()