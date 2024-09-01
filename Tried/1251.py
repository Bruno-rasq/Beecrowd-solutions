# tell me the frequencies

'''
 escreva um algoritmo que receba uma lista de caracteres e retorne uma lista contendo 
 o valor em ASCII do do caracter e quantas vezes ele aparece na lista

 a lista contem varios casos de teste, printe para cada caso de teste a lista de 
frequencias

[exemplo]

input:
 AAABBC
 122333

output:
 67 1
 66 2
 65 3

 49 1
 50 2
 51 3

 função ord() retorna o valor em ASCII do argumento 
 
'''

INPUT = ["AAABBC", "122333"]

def entrada_lista(lista):
    for item in lista:
        yield item

entrada = entrada_lista(INPUT)


cases = []
while True:
    try:
        caso = next(entrada)
        if caso == "":
            break
        else:
            cases.append(caso)
    except StopIteration:
        break

def frequencies(case):
  freq = {}

  for i in list(case):
    item = ord(i)
    if item in freq:
      freq[item] += 1
    else:
      freq[item] = 1

  contagem_ordenada = sorted(freq.items(), key=lambda x: x[1])

  for chave, valor in contagem_ordenada:
    print("{} {}".format(chave, valor))

for case in cases:
  frequencies(case)
  print()