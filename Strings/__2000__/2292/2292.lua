-- Com base no estado atual do led e quantas vezes ele pisca dá para
-- calcular de forma modular qual será seu estado final
local function Toggle_state(led_state, step)
    local STATES = {'X', 'O'}
    local on_off = 0
    if led_state == 'O' then on_off = 1 end
    local state = (on_off + step) % 2
    return STATES[state + 1]
end

-- Com base na quantidade de trocas de estado de um led é possível calcular
-- a quantidade de vezes que ele vai apagar, sendo a quantidade de trocas / 2
-- o valor é truncado caso led esteja inicialmente apagado, ou arredondado
-- caso esteja inicialmente aceso
local function N_toggles(led, step)
    local result = led == 'X' and math.floor(step / 2) or math.ceil(step / 2)
    return result
end

-- Para cada led da esquerda para a direita devo trocar o estado atual para o
-- estado final do led, a quantidade de vezes que o led apagar será a qnt de
-- vezes que o próximo led vai trocar de estado e assim sucessivamente.
local function END_LED_STATE(LEDS, step)
    local ANS = ""
    for i = 1, #LEDS do
        local led = LEDS:sub(i, i)
        ANS = ANS .. Toggle_state(led, step)
        step = N_toggles(led, step)
    end
    print(ANS)
end

-- roda o código.
local N = tonumber(io.read())
for i = 1, N do
    local leds, steps = io.read():match("(%S+) (%S+)")
    END_LED_STATE(leds, tonumber(steps))
end