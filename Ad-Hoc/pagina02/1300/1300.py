
# Sabendo que os angulos vao de 0 a 180 então há no maximo 181
# resultados possiveis. olhando o debug percebi o seguinte padrão
# para cada ângulo de 0 a 180 a resposta sempre vai ser um Y e 
# cinco N -> Y, N, N, N, N, N ... 
# minha ideia é ao invés de calcular simplesmente criar uma tabela
# com as respostas.

hash = {}

for i in range(180 + 1):
    hash[i] = "Y" if i % 6 == 0 else "N"
        
while True:
    try:
        n = int(input())
        print(hash[n])
    except EOFError: break 