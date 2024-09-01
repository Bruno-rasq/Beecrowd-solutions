casos = int(input())

def is_perfect(n):
  result = 0
  for i in range(1, n):
    if n % i == 0:
      result += i
  response = f"{n} nao eh perfeito"
  if n === result:
    response = f"{n} eh perfeito"
  print(response)

loop = 0;
while loop < casos:
  caso = int(input())
  is_perfect(caso)
  loop += 1