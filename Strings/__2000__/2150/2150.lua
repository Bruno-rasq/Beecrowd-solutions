while true do
    
    local chars = io.read()
    if chars == nil then break end
    
    local str = io.read()
    if str == nil then break end
    
    local COUNT = 0
    local HASH = {}
    
    for i = 1, #str do 
        local char = str:sub(i, i)
        HASH[char] = (HASH[char] or 0) + 1
    end

    for i = 1, #chars do
        local char = chars:sub(i, i)
        COUNT = COUNT + (HASH[char] or 0)
    end

    print(COUNT)
end 