local startHour = io.read("*n")
local startMinute = io.read("*n")
local endHour = io.read("*n")
local endMinute = io.read("*n")

local startTime = startHour * 60 + startMinute
local endTime = endHour * 60 + endMinute

local diff

if startTime == endTime then
    diff = 24 * 60
elseif endTime > startTime then
    diff = endTime - startTime
else
    diff = (24 * 60 - startTime) + endTime
end

local hours = diff // 60
local minutes = diff % 60

print(string.format(
    "O JOGO DUROU %d HORA(S) E %d MINUTO(S)",
    hours,
    minutes
))