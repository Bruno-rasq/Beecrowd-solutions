CASES = int(input())

SYSTEM = [
  'PROXYCITY', 
  'P.Y.N.G.', 
  'DNSUEY!',
  'SERVERS', 
  'HOST!', 
  'CRIPTONIZE',
  'OFFLINE DAY', 
  'SALT', 
  'ANSWER!',
  'RAR?', 
  'WIFI ANTENNAS'
]

for _ in range(CASES):
  x, y = [int(x) for x in input().strip().split(' ')]
  opcao = x + y
  print(SYSTEM[opcao])