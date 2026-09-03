def cifra(msg, key):
  letras = "abcdefghijklmnopqrstuvwxyz"
  resposta = ""
  for char in msg:
    indice = letras.index(char.lower())
    novo_indice = (indice - key) % len(letras)
    resposta += letras[novo_indice]
  return resposta
  
itr = 0
casos = int(input())
while itr < casos:
  msg = input()
  key = int(input())
  print(cifra(msg, key))
  itr += 1