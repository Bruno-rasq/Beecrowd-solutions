entrada = input()
veiculos_faltantes = 0
turistas_faltantes = 0 
while entrada != "ABEND":
    operacao, turistas = entrada.split()
    
    turistas = int(turistas)
    
    if operacao == "SALIDA":
        veiculos_faltantes += 1
        turistas_faltantes += turistas
    else:
        veiculos_faltantes -= 1
        turistas_faltantes -= turistas
        
    entrada = input()
    
print(turistas_faltantes)
print(veiculos_faltantes)