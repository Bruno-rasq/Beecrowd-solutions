def create_list(n: int):
  return list(range(1, n + 1))

def josephusProblem(lista, k):
  index = 0
  while len(lista) > 1:
    lista.pop(index)
    index = (index + k - 1) % len(lista)
  return lista[0]

def powerCrisis(n: int):
  lista = create_list(n)
  response = 0
  count = 0
  while response == 0:
    copy = lista.copy()
    result = josephusProblem(copy, count)
    count += 1
    if result == 13:
      response = count
  print(response - 1)

n = int(input())
while n != 0:
  powerCrisis(n)
  n = int(input())