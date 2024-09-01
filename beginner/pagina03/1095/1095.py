import os

os.system('clear')

# sequence IJ3

'''
crie um programa que exibia a seguinte sequência 

I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13

o programa não possue input

'''
i = 1
j = 7
for x in range(0, 5):
  print(f'I={i} J={j}')
  for y in range(0, 2):
    j -= 1
    print(f"I={i} J={j}")

  j += 4
  i += 1 if i % 2 == 0 else 2