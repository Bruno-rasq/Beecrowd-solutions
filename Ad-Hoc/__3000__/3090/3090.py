
#comprimento & largura (campo batalha), n soldados
compri, larg, n_soldados = [int(x) for x in input().split()]

poder_exer_1 = 0
poder_exer_2 = 0

#rio divide o plane em dois hemisférios (0,0)(c,l)
def verificar_hemisferio(x, y, p):
    global compri
    global larg
    global poder_exer_1
    global poder_exer_2
    #equacao da reta y = L/C * x
    if y > (larg / compri) * x:
        poder_exer_1 += p
    elif y < (larg / compri) * x:
        poder_exer_2 += p

for _ in range(n_soldados):
    coord_x, coord_y, poder = [int(x) for x in input().split()]
    verificar_hemisferio(coord_x, coord_y, poder)
    
print(f"{poder_exer_1} {poder_exer_2}")