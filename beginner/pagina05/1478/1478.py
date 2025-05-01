    
while True:
    N = int(input())
        
    if N == 0:
        break
    
    def exibir_line(lista):
        print(" ".join(f"{n:3}" for n in lista))
        
    def espelhar_lista(lista):
        lista.pop()
        novo = lista[0] + 1
        lista.insert(0, novo)
        return lista
    
    curr = [int(x) for x in range(1, N + 1)]
    exibir_line(curr)
    i = 1
    while i < N:
        novo = espelhar_lista(curr)
        exibir_line(novo)
        i+=1
        curr = novo
        
    print()