cases = int(input())

def game(p1, p2):
  if p1 == p2 and p1 == "ataque":
    return "Aniquilacao mutua"
    
  if p1 == p2 and p1 == "pedra":
    return "Sem ganhador"

  if p1 == p2 and p1 == "papel":
    return "Ambos venceram"

  if (p1 == "ataque" and p2 != "ataque") or (p1 == "pedra" and p2 == "papel"):
    return "Jogador 1 venceu"

  if (p2 == "ataque" and p1 != "ataque") or (p2 == "pedra" and p1 == "papel"):
    return "Jogador 2 venceu"

  
for i in range(cases):
  j1 = input()
  j2 = input()

  result = game(j1, j2)
  print(result)