digits = {
    "0": ["***", "* *", "* *", "* *", "***"],
    "1": ["  *", "  *", "  *", "  *", "  *"],
    "2": ["***", "  *", "***", "*  ", "***"],
    "3": ["***", "  *", "***", "  *", "***"],
    "4": ["* *", "* *", "***", "  *", "  *"],
    "5": ["***", "*  ", "***", "  *", "***"],
    "6": ["***", "*  ", "***", "* *", "***"],
    "7": ["***", "  *", "  *", "  *", "  *"],
    "8": ["***", "* *", "***", "* *", "***"],
    "9": ["***", "* *", "***", "  *", "***"],
}

# Lê as 5 linhas da entrada
lines = [input() for _ in range(5)]

# Calcula quantos dígitos tem
num_digits = (len(lines[0]) + 1) // 4  # 3 chars + 1 espaço por dígito

result = ""
valid = True

# Para cada dígito
for i in range(num_digits):
    start = i * 4
    bloco = [linha[start:start+3] for linha in lines]

    found = False
    for digit, pattern in digits.items():
        if bloco == pattern:
            result += digit
            found = True
            break

    if not found:
        valid = False
        break

# Verifica validade
if not valid or int(result) % 6 != 0:
    print("BOOM!!")
else:
    print("BEER!!")