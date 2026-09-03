tabela_codigos = {}
for i in range(26):
    letra = chr(97 + i)  # minúsculas: 'a' = 97
    ciclo = i // 3 + 1
    pontos = '.' * ((i % 3) + 1)
    criptografado = ' '.join([pontos] * ciclo)
    tabela_codigos[criptografado] = letra
    
while True:
    try:
        n = int(input()) #numero de caracteres na mensagem
        for _ in range(n):
            codigo = input()
            print(tabela_codigos.get(codigo))
    except EOFError:
        break