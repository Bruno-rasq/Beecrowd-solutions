#numero de figurinhas no album 
#numero de figurinhas carimbadas
#numero de figurinhas compradas
NF, FC, NFC = [int(x) for x in input().split()] # NF é meio inutil :( 

figurinhas_carimbadas = [int(x) for x in input().split()]
figurinhas_compradas = [int(x) for x in input().split()]

album = {}
figurinhas_carimbadas_faltantes = FC

for i in range(NFC):
    figurinha = figurinhas_compradas[i]
    if figurinha not in album:
        album[figurinha] = True

for figurinha in list(album):
    if figurinha in figurinhas_carimbadas:
        figurinhas_carimbadas_faltantes -= 1
        
print(figurinhas_carimbadas_faltantes)