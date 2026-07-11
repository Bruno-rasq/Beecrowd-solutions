-- Ascii a-z -> 97 - 122
local function main() 
    local n = tonumber(io.read())
    local chr = string.char(96 + n)
    print(chr)
end

main()