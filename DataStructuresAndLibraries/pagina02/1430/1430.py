NOTAS = {
  "w": 1,
  "h": 0.5,
  "q": 0.25,
  "e": 0.125,
  "s": 0.0625,
  "t": 0.03125,
  "x": 0.015625
}

def separar_compassos(entrada):
  data = entrada[1:-1]
  return data.split("/")

while True:
  try:
    entrada=input().lower()

    if entrada == "*":
      break

    acertos=0
    compassos=separar_compassos(
      entrada
    )
    
    for compasso in compassos:
      duracao = 0.0
      for nota in compasso:
        duracao += NOTAS[nota]
      if duracao == 1:
        acertos += 1
      
    print(acertos)
  except EOFError:
    break