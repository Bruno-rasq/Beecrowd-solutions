#dado uma entrada precisa corrigir um erro fatal, para isso
#ignore espacos em branco e caracter A-Z a-z e caracteres
#especiais como vigula, pont e etc...

#se o caracter for "l" trate como 1
#se caracter for O ou o trata como 0
#nenhum valor deve ser maior que 2147483647
#se não tiver valor inteiro ou não satisfazer os requisitos
#print error

valor_maximo = 2147483647

while True:
    try:
        n = input()
        num = ""
        is_valid = True

        for char in n:
            if char.isdigit():
                num += char
            elif char in ['O', 'o']:
                num += '0'
            elif char == 'l':
                num += '1'
            elif char in [' ', ',']:
                continue
            else:
                is_valid = False
                break

        error = num == "" or int(num) > valor_maximo
        print(int(num) if (not error and is_valid) else "error")
    
    except EOFError:
        break