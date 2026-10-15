local first_test_case = true

while true do
    local n = tonumber(io.read())
    if n == 0 then break end

    local data = {
        ["branco"] = {["P"] = {}, ["M"] = {}, ["G"] = {}},
        ["vermelho"] = {["P"] = {}, ["M"] = {}, ["G"] = {}},
    }

    for i = 1, n do
        local name = io.read()
        local color, size = io.read("*l"):match("(%S+) (%S+)")
        table.insert(data[color][size], name)
    end

    if not first_test_case then print("") end
    first_test_case = false

    for color in pairs(data) do
        for size in pairs(data[color]) do
            table.sort(data[color][size])

            for _, name in ipairs(data[color][size]) do
                print(string.format("%s %s %s", color, size, name))
            end
        end
    end
end