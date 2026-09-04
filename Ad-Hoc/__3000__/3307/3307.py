import math
def calcular_raio(area):
    raio = math.sqrt(area / (4 * 3.14))
    return raio
    
num_esferas = int(input())
for _ in range(num_esferas):
    area = int(input())
    raio = calcular_raio(area)
    
    if raio < 12: # vermelho R$0.09
        valor = area * 0.09
        print(f"vermelho = R$ {valor:.2f}")
     
    elif 12 <= raio <= 15: # azul R$0.07
        valor = area * 0.07
        print(f"azul = R$ {valor:.2f}")
       
    elif raio > 15: # amarelo R$0.05
        valor = area * 0.05
        print(f"amarelo = R$ {valor:.2f}")