n = int(input())

elephants = 0
for i in range(n):
    if i % 2 == 0:
        elephants += i
    else:
        elephants += 1

print(elephants) 