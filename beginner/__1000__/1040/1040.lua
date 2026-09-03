local a, b, c, d = io.read():match("(%S+) (%S+) (%S+) (%S+)")
a, b, c ,d = tonumber(a), tonumber(b), tonumber(c), tonumber(d)

local avg = (a * 2 + b * 3 + c * 4 + d * 1) / 10

print(string.format("Media: %.1f", avg))
if avg >= 7.0 then 
    print("Aluno aprovado.")
elseif avg >= 5.0 and avg <= 6.9 then
    print("Aluno em exame.")
    local exame = tonumber(io.read())
    avg = (avg + exame) / 2
    print(string.format("Nota do exame: %.1f", exame))
    if avg >= 5.0 then 
        print("Aluno aprovado.")
    else
        print("Aluno reprovado.")
    end
    print(string.format("Media final: %.1f", avg))
else 
    print("Aluno reprovado.")
end