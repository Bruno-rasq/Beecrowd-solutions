nokia_keyboard = {
    "a": "2", "b": "22", "c": "222",
    "d": "3", "e": "33", "f": "333",
    "g": "4", "h": "44", "i": "444",
    "j": "5", "k": "55", "l": "555",
    "m": "6", "n": "66", "o": "666",
    "p": "7", "q": "77", "r": "777", "s": "7777",
    "t": "8", "u": "88", "v": "888",
    "w": "9", "x": "99", "y": "999", "z": "9999",
    " ": "0"
}

n_mensagem = int(input())

for _ in range(n_mensagem):
    mensagem = input()
    resultado = ""
    anterior_tecla = ""
    
    for char in mensagem:
        is_upper = char.isupper()
        tecla = nokia_keyboard[char.lower()]
        
        # Se o primeiro número da tecla atual é igual à última tecla usada
        conflito = (anterior_tecla == tecla[0])
        
        if conflito:
            if not is_upper:
                resultado += "*"
            # Se for maiúsculo, o "#" já separa, então não precisa do "*"
        
        if is_upper:
            resultado += "#"
        
        resultado += tecla
        anterior_tecla = tecla[-1]  # Atualiza para o último dígito da tecla atual
    
    print(resultado)