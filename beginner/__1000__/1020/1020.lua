local value = tonumber(io.read())
local years = math.floor(value / 365)
value = value % 365
local months = math.floor(value / 30)
value = value % 30
local days = value


print(string.format("%d ano(s)", years))
print(string.format("%d mes(es)", months))
print(string.format("%d dia(s)", days))