import os

os.system('clear')

# A long long time ago

'''
escreva um algoritmo que com base em uma data fornecida calcule em que momento da 
história o fato aconteceu.

levando em consideração o ano atual como sendo 2015:

15 => 2000 D.C
10000 => 7986 A.C

'''

INPUT = ["3", "10000", "15", "2015"]

iterador = int(INPUT.pop(0))

for i in range(iterador):
  T = int(INPUT.pop(0))

  T = 2015 - T

  if T <= 0:
    print(f"{1 - T} A.C.")
  else:
    print(f"{T} D.C.")