local function main()
    local eve = 0
    local odd = 0
    local pos = 0
    local neg = 0
    for i=1, 5 do
        local n = tonumber(io.read())
        if n % 2 == 0 then eve = eve + 1 end
        if n % 2 ~= 0 then odd = odd + 1 end
        if n > 0 then pos = pos + 1 end
        if n < 0 then neg = neg + 1 end
    end
    print(string.format("%d valor(es) par(es)", eve))
    print(string.format("%d valor(es) impar(es)", odd))
    print(string.format("%d valor(es) positivo(s)", pos))
    print(string.format("%d valor(es) negativo(s)", neg))
end

main()