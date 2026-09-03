import math 

a, b = list(
  map(int, input().split(" "))
)

def calcula(x, y):
  quo=0

  if (x > 0 and y > 0) or (x < 0 and y > 0):
    quo = x//y
  else:
    quo = math.ceil(x/y)

  return f'{quo} {x - (y * quo)}'

print(calcula(a,b))