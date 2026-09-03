local a, b, c, d = io.read():match("([%-]?%d+) ([%-]?%d+) ([%-]?%d+) ([%-]?%d+)")
a, b, c, d = tonumber(a), tonumber(b), tonumber(c), tonumber(d)

if b > c
    and d > a
    and (c + d) > (a + b)
    and c >= 0
    and d >= 0
    and (a % 2 == 0)
then
    print("Valores aceitos")
else
    print("Valores nao aceitos")
end