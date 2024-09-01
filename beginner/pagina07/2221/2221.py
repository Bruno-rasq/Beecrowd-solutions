CASES=int(input())

def setup_data(inp):
  return list(map(int, inp.split(" ")))

for _ in range(CASES):
  bonus = int(input())
  da, dd, nd = setup_data(input())
  ga, gd, ng = setup_data(input())

  valorg = (ga + gd) / 2
  valord = (da + dd) / 2
  
  if nd % 2 == 0:
    valord += bonus

  if ng % 2 == 0:
    valorg += bonus

  if valorg > valord:
    print('Guarte')
  elif valord > valorg:
    print('Dabriel')
  elif valord == valorg:
    print('Empate')