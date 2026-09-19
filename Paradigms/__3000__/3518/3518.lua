local N, K = io.read("*n", "*n")
local times = {}

for i = 1, N do
    times[i] = io.read("*n")
end

local LEFT = 1
local SUM = 0
local ANS = 0

for RIGHT = 1, N do
    SUM = SUM + times[RIGHT]

    while SUM > K do
        SUM = SUM - times[LEFT]
        LEFT = LEFT + 1
    end

    ANS = math.max(ANS, RIGHT - LEFT + 1)
end

print(ANS)