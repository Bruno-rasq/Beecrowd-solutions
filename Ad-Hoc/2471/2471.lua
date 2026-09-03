-- PARA CADA LINHA COLUNA, CALCULO A SOMA DE AMBAS AO MESMO TEMPO
-- SE AS DUAS TIVEREM A MESMA SOMATÓRIA ENTÃO OK, DO CONTRÁRIO UM
-- DOS VALORES ESTÁ ERRADO.

local N = tonumber(io.read())
local matrix = {}
local row_sum = {}
local col_sum = {}

-- Inicializa as somas das colunas
for j = 1, N do col_sum[j] = 0 end

-- LÊ OS INPUTS ENQUANTO CALCULA A SOMATÓRIA DAS LINHAS E COLUNAS
for i = 1, N do
    matrix[i] = {}
    row_sum[i] = 0
    local j = 1

    for num in io.read():gmatch("%S+") do
        local value = tonumber(num)

        matrix[i][j] = value
        row_sum[i] = row_sum[i] + value
        col_sum[j] = col_sum[j] + value
        j = j + 1
    end
end

-- Encontra a soma correta.
-- Procuramos uma soma de linha que também aparece nas colunas.
local correct_sum

for i = 1, N do
    for j = 1, N do
        if row_sum[i] == col_sum[j] then
            correct_sum = row_sum[i]
            break
        end
    end

    if correct_sum then
        break
    end
end

-- Procura a linha cuja soma está errada
local wrong_row

for i = 1, N do
    if row_sum[i] ~= correct_sum then
        wrong_row = i
        break
    end
end

-- Procura a coluna cuja soma está errada
local wrong_col

for j = 1, N do
    if col_sum[j] ~= correct_sum then
        wrong_col = j
        break
    end
end

-- Pega o valor errado
local wrong_value = matrix[wrong_row][wrong_col]

-- Calcula qual deveria ser o valor correto
local correct_value = wrong_value + correct_sum - row_sum[wrong_row]

io.write(correct_value .. " " .. wrong_value .. "\n")