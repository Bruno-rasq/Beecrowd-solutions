#tamanho containers
largura_c, comprimento_c, altura_c, = [int(x) for x in input().split()]
#tamanho mavio
largura_n, comprimento_n, altura_n, = [int(x) for x in input().split()]

if (largura_c > largura_n) or (altura_c > altura_n) or (comprimento_c > comprimento_n):
    print(0)
else:
    #quantos containers cabem
    x = largura_n // largura_c
    y = comprimento_n // comprimento_c
    z = altura_n // altura_c
    
    quantidade_containers = x * y * z 
    print(quantidade_containers)