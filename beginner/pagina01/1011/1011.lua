local Pi = 3.14159
local raio = tonumber(io.read())
local sphereArea = (4.0 / 3.0) * Pi * (raio * raio * raio)

print("VOLUME = " .. string.format("%.3f", sphereArea))