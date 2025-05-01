n_runas, gollum = [int(x) for x in input().split()]

runas = {}

for _ in range(n_runas):
    runa, valor = input().split()
    runas[runa] = int(valor)
    
n_runas_sam_frodo = int(input())
poder = 0
runas_sam_frodo = input().split()

for i in range(n_runas_sam_frodo):
    runa = runas_sam_frodo[i]
    poder += runas[runa]
    
print(poder)
print("You shall pass!" if poder >= gollum else "My precioooous")