import math 

# Bhaskara's Formula

'''
escreva um programa que leia 3 float numbers e qualcule as raizes de uma 
equação de segundo grau

'''

text = "10.0 20.1 5.1"
input = text.split(' ')

a = float(input[0])
b = float(input[1])
c = float(input[2])

delta = (b * b) - (4 * a * c) 

if delta >= 0 and a != 0:
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)

  output = "{} = {}"
  print(output.format('R1', "{:.5f}".format(x1)))
  print(output.format('R2', "{:.5f}".format(x2)))

else:
  print("Impossivel calcular")