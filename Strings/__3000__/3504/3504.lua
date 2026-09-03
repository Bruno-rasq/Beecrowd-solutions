local sentense = io.read()

local ptr1 = 1
local ptr2 = #sentense
local isPalindrome = true
while ptr1 ~= ptr2 do
    if sentense:sub(ptr1, ptr1) ~= sentense:sub(ptr2, ptr2) then
        isPalindrome = false
        break
    end
    ptr1 = ptr1 + 1
    ptr2 = ptr2 - 1
end

if not isPalindrome then 
    print(string.format("A frase [%s] nao eh palindrome", sentense))
end
if isPalindrome then
    print(string.format("A frase [%s] eh palindrome", sentense))
end