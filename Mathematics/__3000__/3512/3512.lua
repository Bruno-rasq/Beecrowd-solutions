local A, Y, F, P = io.read("*n", "*n", "*n", "*n")

if A % Y == 0 then
    print(0)
else
    local days_forward = ((Y - A%Y)% Y) * F
    local days_backward = (A % Y) * P

    print(math.min(days_backward, days_forward))
end