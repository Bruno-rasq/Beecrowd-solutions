-- Serie de leds controlados por um botão:
-- Ao clicar no botão o led mais a direita troca de estado.
-- ("O" on && "-" off)

-- Caso o led apague, o led adjacente esquerdo dele troca de estado.
-- Se o led esquerdo ascender então ele propaga a troca até que um
-- led se apague.

local numberLeds = tonumber(io.read())
local currentLedInput = io.read()
local targetLedStates = io.read()
local currentLedStates = {}
local totalClicks = 0

-- Altera o estado do led de acesso para apagado e vice-versa.
local function ToggleState(led)
    if led == "O" then return "-" end
    if led == "-" then return "O" end
end

for i = 1, numberLeds do
    currentLedStates[i] = currentLedInput:sub(i, i)
end

-- Reconstrói a string para comparar com o objetivo
local function GetLedStates()
    return table.concat(currentLedStates)
end

while GetLedStates() ~= targetLedStates do
    totalClicks = totalClicks + 1

    currentLedStates[numberLeds] = ToggleState(currentLedStates[numberLeds])

    if currentLedStates[numberLeds] == "-" then
        local currentLed = numberLeds - 1

        while currentLed >= 1 do
            currentLedStates[currentLed] = ToggleState(currentLedStates[currentLed])

            if currentLedStates[currentLed] == "O" then
                break
            end

            currentLed = currentLed - 1
        end
    end
end

print(totalClicks)