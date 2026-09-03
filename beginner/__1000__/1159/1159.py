a = int(input())

def sum_evens(n):
  result = 0
  count = 0
  while count < 5:
    if n % 2 == 0:
      result += n
      count += 1
    n += 1
  return result

while a != 0:
  print(sum_evens(a))
  a = int(input())