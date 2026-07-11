local n = tonumber(io.read())

local function isPowerOfTwo(n)
    return n > 0 and (n & (n - 1)) == 0
end

if isPowerOfTwo(n) then
    print("true")
else
    print("false")
end