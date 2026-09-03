cases = int(input())

gifts = 0
restB = 0
restA = 0
restM = 0
restD = 0

for i in range(cases):
    name, group, h = input().split()
    hours = int(h)

    if group == 'bonecos':
        gifts += (hours + restB) // 8
        restB = (hours + restB) % 8
    
    elif group == 'arquitetos': 
        gifts += (hours + restA) // 4
        restA = (hours + restA) % 4
     
    elif group == 'musicos':
        gifts += (hours + restM) // 6
        restM = (hours + restM) % 6
     
    else: 
        gifts += (hours + restD) // 12
        restD = (hours + restD) % 12
     

print(gifts)