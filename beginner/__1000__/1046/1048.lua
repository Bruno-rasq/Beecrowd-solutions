local startTime = io.read("*n")
local endTime = io.read("*n")

if startTime == endTime then 
    print("O JOGO DUROU 24 HORA(S)")

else 
    local duration = 0
    while startTime ~= endTime do
        startTime = (startTime + 1) % 24
        duration = duration + 1
    end
    
    print(string.format("O JOGO DUROU %d HORA(S)", duration))
end