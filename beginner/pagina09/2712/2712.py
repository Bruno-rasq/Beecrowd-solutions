# Tabela semana e últimos dígitos
tabela = [
    ["MONDAY", 1, 2],
    ["TUESDAY", 3, 4],
    ["WEDNESDAY", 5, 6],
    ["THURSDAY", 7, 8],
    ["FRIDAY", 9, 0]
]

n = int(input())  # Número de placas a se verificar

for _ in range(n):
    entrada = input().strip()
    
    if "-" in entrada:
        placa = entrada.split("-")
        
        # Verifica formato: parte antes do "-" tem 3 letras maiúsculas
        # Parte depois tem 4 dígitos
        if (
            len(placa) == 2 and
            len(placa[0]) == 3 and placa[0].isalpha() and placa[0].isupper() and
            len(placa[1]) == 4 and placa[1].isdigit()
        ):
            ultimo_digito = int(placa[1][-1])
            for dia in tabela:
                if ultimo_digito in dia[1:]:
                    print(dia[0])
                    break
        else:
            print("FAILURE")
    else:
        print("FAILURE")