
#objetivo calcular o grau de dificuldade de uma questão baseada
#na media da quantidade de palavrass e atribuir uma pontuacao

#questoes com media igual ou abaixo de 3 recebem 250 pontos.
#questoes com media maior que 3 e menor ou igual a 6 500 pontos.
#media acima de 6 recebem 1000 pontos.

def media_frase(line):
    total_palavras = 0
    somatoria_palavras = 0

    for palavra in line:
        if palavra.endswith('.'):
            palavra_limpa = palavra[:-1]
        else:
            palavra_limpa = palavra

        if palavra_limpa.isalpha():
            somatoria_palavras += len(palavra_limpa)
            total_palavras += 1

    if total_palavras == 0:
        return 0

    return somatoria_palavras // total_palavras
    
    
while True:
    try:
    
        line = input().split()
        media = media_frase(line)
        
        print(250 if media <= 3.0 else (500 if  3.0 < media <= 5.0 else 1000))
    except EOFError:
        break