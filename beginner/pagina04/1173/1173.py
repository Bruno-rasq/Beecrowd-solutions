# array fill I

'''
 crie um programa que leia um numero inteiro N e preencha um vetor com 10 posições 
 onde a primeira posição recebe o valor de N e as demais recebem o dobro do valor

 [exemplo]

 input:
   1

 output:
  N[0] = 1
  N[1] = 2
  N[2] = 4
  ...
  N[9] = 18
'''

x = 1 #int(input())

for i in range(10):
  print("N[{}] = {}".format(i, x))
  x *= 2