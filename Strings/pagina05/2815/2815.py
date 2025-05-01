
texto = input().split()

texto_corrigido = []
for palavra in texto:
    if len(palavra) > 4:
        silaba1 = palavra[0] + palavra[1]
        silaba2 = palavra[2] + palavra[3]
        
        if silaba1 == silaba2:
            palavra = palavra[2:] #remove a primeira silaba
            
    texto_corrigido.append(palavra)
print(" ".join(texto_corrigido))