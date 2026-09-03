local BRAILLE = {
    [1] = "*.....", [2] = "*.*...", [3] = "**....",
    [4] = "**.*..", [5] = "*..*..", [6] = "***...",
    [7] = "****..", [8] = "*.**..", [9] = ".**...",
    [0] = ".***.."
}

local function intToStr()
    local input = io.read()

    for line = 1, 3 do
        local output = ""
        local left = (line - 1) * 2 + 1
        local right = left + 1

        for idx = 1, #input do
            local value = tonumber(input:sub(idx, idx))
            local braille = BRAILLE[value]

            if idx > 1 then
                output = output .. " "
            end

            output = output .. braille:sub(left, right)
        end

        print(output)
    end
end

local function strToInt(n)
    local ans = {}

    for line = 1, 3 do
        local idx = 1

        for braille_part in io.read():gmatch("%S+") do
            if not ans[idx] then
                ans[idx] = ""
            end

            ans[idx] = ans[idx] .. braille_part
            idx = idx + 1
        end
    end

    local output = ""

    for idx = 1, n do
        for value = 0, 9 do
            if BRAILLE[value] == ans[idx] then
                output = output .. value
                break
            end
        end
    end

    print(output)
end

while true do
    local n = tonumber(io.read())
    if n == 0 then
        break
    end

    local op = io.read()

    if op == "S" then
        intToStr()
    elseif op == "B" then
        strToInt(n)
    end
end