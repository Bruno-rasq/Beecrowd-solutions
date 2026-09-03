crypt = [
    ["GQaku", "0"],
    ["ISblv", "1"],
    ["EOYcmw", "2"],
    ["FPZdnx", "3"],
    ["JTeoy", "4"],
    ["DNXfpz", "5"],
    ["AKUgq", "6"],
    ["CMWhr", "7"],
    ["BLVis", "8"],
    ["HRjt", "9"]
]

n = int(input())  # Número de senhas
for _ in range(n):
    frase = input()  # Senha que será criptografada
    incrypt = ""
    
    for char in frase:
        if char == " ":
            continue  # Ignora os espaços
        for c in crypt:
            if char in c[0]:  # Se o caractere estiver no conjunto de letras
                incrypt += c[1]  # Adiciona o número correspondente
                
        if len(incrypt) >= 12:  # Se já tiver 12 caracteres, parar de adicionar mais números
            break
    
    print(incrypt[:12])  # Limita o resultado a 12 caracteres