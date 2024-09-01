INPUT = input()
p, j1, j2, r, a = list(map(int, INPUT.split()))

if (r == 1 and a == 0) or (r == 0 and a == 1):
  print('Jogador 1 ganha!')
  
elif r == 1 and a == 1:
  print('Jogador 2 ganha!')
  
else:
  print(f'Jogador {1 if (j1 + j2) % 2 == (1 - p) else 2} ganha!')