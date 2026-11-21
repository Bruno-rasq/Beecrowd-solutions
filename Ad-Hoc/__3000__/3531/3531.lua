local x1, y1, x2, y2, k = io.read("*n", "*n", "*n", "*n", "*n")

local dist = math.abs(y2 - y1) + math.abs(x2 - x1)

if dist <= k then print("SIM") else print("NAO") end