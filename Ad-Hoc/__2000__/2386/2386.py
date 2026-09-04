QNT_FOTONS_PERCEBIVEIS_A_OLHO = 40000000
area_abertura_telescopio = int(input())

x = QNT_FOTONS_PERCEBIVEIS_A_OLHO / area_abertura_telescopio

numero_total_de_estrelas = int(input())
contador_estrelas_visiveis = 0 

for _ in range(numero_total_de_estrelas):
    brilho_estrela_atual = int(input())
    if brilho_estrela_atual >= x:
        contador_estrelas_visiveis += 1
        
print(contador_estrelas_visiveis)