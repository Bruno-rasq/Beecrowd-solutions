a, b = input().split(' ')
a = int(a)
b = int(b)

loop = 1
while loop <= b:
  curr = []
  for i in range(a):
    curr.append(loop)
    loop += 1
  print(" ".join(str(num) for num in curr))
  curr.clear()