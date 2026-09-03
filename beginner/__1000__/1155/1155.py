import os

os.system('clear')

# s sequence

'''
crie um programa que calcule e mostre o valor de s, sendo s = 1 + 1/2 + 1/3 +... 1/100

o output deve conter apenas o valor de s com duas casas decimais

'''

s = 0
for i in range(1, 101):
  s += 1/(i)

print(f"{s:.2f}")