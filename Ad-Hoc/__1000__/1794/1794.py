# laundry

'''
crie um programa que dado uma quantidade de roupas, uma quantidade minima e maxima de 
roupas a serem lavadas e uma quantidade minima e maxima de roupas a serem secadas.
calcule se é possivel lavar todas as roupas ou não.
'''

text = "12"
text2 = "10 11"
text3 = "12 16"

clothes = int(text.strip())
la, lb = map(int, text2.split(' '))
sa, sb = map(int, text3.split(' '))

if la <= clothes <= lb and sa <= clothes <= sb:
  print("possivel")
else:
  print("impossivel")