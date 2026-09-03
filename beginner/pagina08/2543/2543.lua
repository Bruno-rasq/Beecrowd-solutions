while true do
    local N, ID = io.read("*n", "*n")
    if N == nil then break end

    local ans = 0
    for i = 1, N do
        local id, game = io.read("*n", "*n")
        if id == ID and game == 0 then
            ans = ans + 1
        end
    end

    print(ans)
end