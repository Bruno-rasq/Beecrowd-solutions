
#objetivo é calcular a quantidade de pets com as condições 
#necesswrias para Carmem poder adota-lod.

#condicoes:
#deve ser cachorro
#deve ter nome composto
#pelo menos uma das palavras do seu nome deve conter a mesma
#inicial da raça

def inicial_valida(raca, nome):
    for palavra in nome:
        char = palavra[0]
        primeira_char_raca = raca[0]
        if char == primeira_char_raca:
            return True
    return False

while True:
    try:
        pets_disponiveis = int(input())
        pets_validos = 0
        
        for _ in range(pets_disponiveis):
            especie = input()
            raca = input()
            nome = input().split()
            input()
            
            inicial = inicial_valida(raca, nome)
            if especie == "cachorro" and len(nome) > 1 and inicial:
                pets_validos += 1
                
        print(pets_validos)
    except EOFError:
        break