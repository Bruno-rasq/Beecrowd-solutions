-- DECLARANDO GLOBALMENTE O TEXTO DE SAÍDA E IMAGEM
local out = {}
local image = {}


-- DESCOBRIR SE UM QUADRANTE É UNIFORME.
-- CASO SIM RETORNA QUAL O PIXEL FORMA O QUADRANTE W/B
-- CASO CONTRÁRIO IMPRIME UM Q E DIVIDE O QUADRANTE EM
-- 4 OUTROS QUADRANTES RECURSIVAMENTE.
local function COMPRESS(x, y, size)
    local top_left_pixel = image[x][y]
    local same_pixel = true
    for i = x, x + size - 1 do
        for j = y, y + size - 1 do
            if image[i][j] ~= top_left_pixel then
                same_pixel = false
                break
            end

        end
        if not same_pixel then
            break
        end
    end

    if same_pixel then
        out[#out + 1] = top_left_pixel
        return
    end

    out[#out + 1] = "Q"
    local half = size // 2
    COMPRESS(x, y, half)
    COMPRESS(x, y + half, half)
    COMPRESS(x + half, y, half)
    COMPRESS(x + half, y + half, half)
end

local n = tonumber(io.read():match("(%d+)$"))
io.read()
io.read()

for i = 1, n do

    image[i] = {}

    local line = io.read()
    local column = 1

    -- CADA HEXADECIMAL REPRESENTA 8 PIXELS
    for hex in line:gmatch("0x(%x+)") do

        local value = tonumber(hex, 16)

        -- XBM ARMAZENA OS PIXELS DO BIT MENOS SIGNIFICATIVO
        -- PARA O MAIS SIGNIFICATIVO.
        for bit = 0, 7 do

            if ((value >> bit) & 1) == 1 then
                image[i][column] = "B"
            else
                image[i][column] = "W"
            end

            column = column + 1
        end
    end
end

COMPRESS(1, 1, n)

print(n)
print(table.concat(out))