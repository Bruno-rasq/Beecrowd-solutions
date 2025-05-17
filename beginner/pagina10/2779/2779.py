n_figurinhas_album = int(input())
n_figurinhas_compradas = int(input())

album = {}

for _ in range(n_figurinhas_compradas):
    figurinha = int(input())
    if figurinha not in album:
        album[figurinha] = True
    
print(n_figurinhas_album - len(album))