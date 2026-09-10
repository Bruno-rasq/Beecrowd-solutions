local N = tonumber(io.read())
local M = tonumber(io.read())

local G = math.abs((M - 4 * N) / -2)
local T = N - G

print(string.format("%d", T))
print(string.format("%d", G))