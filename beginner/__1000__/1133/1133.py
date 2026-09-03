n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1

for ele in range(n1 + 1, n2):
    if ele % 5 == 2 or ele % 5 == 3:
        print(ele)