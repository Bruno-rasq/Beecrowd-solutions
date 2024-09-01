
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def josephsCousins(n: int):
  primos = prime_generator()
  lista = list(range(1, n + 1))
  
  pos = 0
  while len(lista) > 1:
    idx = next(primos) - 1
    pos = (pos + idx) % len(lista)
    lista.pop(pos)
    
  return lista[0]


num = int(input())
while num != 0:
  response = josephsCousins(num)
  print(response)
  num = int(input())