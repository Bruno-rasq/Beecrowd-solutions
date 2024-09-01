CASES=int(input())

RESULTADOS = {
  'pedra'  : ['tesoura', 'lagarto'],
  'tesoura': ['papel', 'lagarto'],
  'papel'  : ['pedra', 'spock'],
  'lagarto': ['spock', 'papel'],
  'spock'  : ['tesoura', 'pedra']
}

#rock paper scissor lizard spock
def RPSLS(idx, s, r):
  if s == r:
    print(f"Caso #{idx + 1}: De novo!")
  elif r in RESULTADOS.get(s, []):
    print(f"Caso #{idx + 1}: Bazinga!")
  else:
    print(f"Caso #{idx + 1}: Raj trapaceou!")
      

for idx in range(CASES):
  Sheldon, Raj = input().split(" ")
  RPSLS(
    idx, 
    Sheldon.lower(), 
    Raj.lower()
  )