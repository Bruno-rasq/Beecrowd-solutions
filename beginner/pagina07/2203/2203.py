"""
  --colinha:

  xf = cood fiddlesticks
  yf = cood fiddlesticks
  xi = cood invasor
  yi = cood invasor
  vi = velocídade do invasor
  r1 = raio final 
  r2 = raio do crowstorm

  --TEST CASES:
  4 6 22 6 0 16 2
  4 6 22 6 1 16 2
"""
import math

def calcular_distancia(x1, y1, x2, y2):
  return math.sqrt(
    (x2 - x1)**2 + (y2 - y1)**2
  )

def setup_data(input):
  return list(map(
    int,
    input.split(" ")
  ))
  
while True:
  try:
    Xf, Yf, Xi, Yi, Vi, R1, R2 = setup_data(input())

    distancia_percorrida = Vi * 1.5
    distancia = calcular_distancia(
      Xf, Yf, Xi, Yi
    )

    if (R1 + R2) >= (distancia + distancia_percorrida):
      print("Y")
    else:
      print("N")

  
  except EOFError:
    break