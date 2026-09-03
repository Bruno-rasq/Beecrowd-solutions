renas = [
    "Dasher", "Dancer", "Prancer", 
    "Vixen", "Comet", "Cupid", 
    "Donner", "Blitzen", "Rudolph"
]

bolas_de_neve = [int(x) for x in input().split()]
total = sum(bolas_de_neve)

escolhido = 0
i = 0
while True:
    escolhido = i % len(renas)
    total -= 1
    i += 1
    if total == 0:
        break
    
print(renas[escolhido])