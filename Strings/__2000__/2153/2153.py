
#dada uma string devo remover as silabas ou caracteres que se
#repetem. um padrão das strings é que todas possuem caracteres
#diferentes até que comecem a se repetir.

#a ideia é inverter a palavra e ir dividindo entre a parte inicial
#do inico até a posição i da palvra (a) e a parte final que vai da
#posicao i até o final da palavra (b). depois verificar se (a) é 
#igual a parte inicial de B.


while True:
    try:
        palavra = input()
        resposta = palavra
        palavra_invertida = palavra[::-1]
        
        for i in range(1, len(palavra_invertida)):
            a = palavra_invertida[:i]
            b = palavra_invertida[i:]
            if a == b[:len(a)]:
                resposta = b[::-1]
        
        print(resposta)
    except EOFError:
        break