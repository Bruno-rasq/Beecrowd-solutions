# Cria a tabela de "sorte" para as letras do alfabeto de forma modular
# A, J, e S == 1, B, K e T == 2 e assim por diante. 9 é o número máximo.
PYTHAGORIAN_TABLE = {}
luck_number = 1
for ascii_number in range(97, 122 + 1):
    if luck_number == 10: luck_number = 1
    PYTHAGORIAN_TABLE[chr(ascii_number)] = str(luck_number)
    luck_number += 1
PYTHAGORIAN_TABLE[" "] = "" #lida com espaço adicionando um espaço vazio.


def sum_recursive_luck(strlist):
    if len(strlist) == 1: return strlist[0]
    sum = 0
    for digit in strlist:
        sum += int(digit)
    return sum_recursive_luck(str(sum))

while True:
    try:
        INPUT = input()
        luck = ""
        for char in INPUT :
             luck += PYTHAGORIAN_TABLE[char.lower()]
        print(sum_recursive_luck(luck))
    except: break 